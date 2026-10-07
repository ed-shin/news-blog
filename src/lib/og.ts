// 글마다 대표 이미지(1200×630). 검색·디스커버·카카오톡 같은 공유 카드에 쓰인다.
// 빌드 때 satori가 글자 카드를 SVG로 그리고 sharp가 PNG로 바꾼다(src/pages/og/[...slug].png.ts).
// 카드에는 글에 이미 실린 것만 넣는다. 일일은 헤드라인과 1면 지표 네 개,
// 주간 흐름·기획은 제목과 대표 숫자(highlights) 세 개, 용어는 이름과 설명이다.
import satori from 'satori';
import sharp from 'sharp';
import { readFileSync } from 'node:fs';
import { join } from 'node:path';
import { kindOf, headlineOf, type Post } from './posts';
import type { Term } from './terms';

// 빌드는 저장소 맨 위에서 돈다. 번들된 파일 기준 상대 경로는 빌드 결과 위치에 따라 달라져 쓰지 않는다
const FONT_DIR = join(process.cwd(), 'src/assets/og-fonts');
const font = (name: string) => readFileSync(join(FONT_DIR, name));
const FONTS = [
  { name: 'Hahmlet', data: font('Hahmlet-ExtraBold.ttf'), weight: 800 as const },
  { name: 'Pretendard', data: font('Pretendard-Bold.woff'), weight: 700 as const },
  { name: 'Pretendard', data: font('Pretendard-SemiBold.woff'), weight: 600 as const },
  { name: 'Pretendard', data: font('Pretendard-Medium.woff'), weight: 500 as const },
];
const ICON = `data:image/png;base64,${readFileSync(join(process.cwd(), 'public/apple-touch-icon.png')).toString('base64')}`;

// 사이트 토큰(global.css)과 같은 색
const C = { bg: '#141414', glow: '#262626', text: '#ece6d6', muted: '#a9a9a9', border: '#2e2e2e', accent: '#e2b457', up: '#ff7f6e', down: '#83b3ff' };

// 1면 지표 여섯 개 가운데 카드에 싣는 넷. 이름은 일일 글 front.markets와 같아야 한다
const CARD_MARKETS = ['코스피', '원/달러', '미 10년물', '브렌트'];

type Stat = { label: string; value: string; change?: string; note?: string };
type Card = { kind: string; when: string; headline: string; sub?: string; stats?: Stat[]; asOf?: string; term?: boolean };

type Node = { type: string; props: Record<string, unknown> };
const box = (style: Record<string, unknown>, ...children: (Node | null | undefined)[]): Node =>
  ({ type: 'div', props: { style: { display: 'flex', ...style }, children: children.filter(Boolean) } });
const text = (style: Record<string, unknown>, value: string): Node => ({ type: 'div', props: { style, children: value } });
// 한 줄을 넘으면 말줄임표로 자른다(칸이 좁은 라벨·설명용. 숫자 값에는 쓰지 않는다)
const oneLine = { whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' };

// 줄은 빈칸에서만 바꾼다. satori는 keep-all을 줘도 "원/달러", "5%를", "물가(" 안에서 줄을 바꿔서,
// 낱말을 하나씩 놓고 넘치는 낱말을 다음 줄로 보낸다. 한 글자 낱말("미 10년물"의 "미")은 뒤 낱말과 붙인다
function words(value: string, style: Record<string, unknown>): Node {
  const units: string[] = [];
  for (const w of value.split(/\s+/).filter(Boolean)) {
    const last = units.at(-1);
    if (last !== undefined && [...last].length === 1) units[units.length - 1] = `${last} ${w}`;
    else units.push(w);
  }
  const gap = Math.round((style.fontSize as number) * 0.27);
  return box({ flexWrap: 'wrap', columnGap: gap }, ...units.map((u) => text({ ...style, whiteSpace: 'nowrap' }, u)));
}

function headlineSize(s: string, term?: boolean) {
  const n = [...s].length;
  if (term) return n <= 8 ? 96 : 80;
  return n <= 22 ? 70 : n <= 32 ? 62 : n <= 44 ? 56 : n <= 56 ? 50 : 46;
}

function layout({ kind, when, headline, sub, stats, asOf, term }: Card): Node {
  const top = box({ justifyContent: 'space-between', alignItems: 'center' },
    box({ alignItems: 'center', gap: 16 },
      { type: 'img', props: { src: ICON, width: 52, height: 52, style: { borderRadius: 12 } } },
      box({ alignItems: 'baseline', fontFamily: 'Hahmlet', fontWeight: 800, fontSize: 30, color: C.text, letterSpacing: 1 },
        text({}, '견문록'), text({ color: C.muted, margin: '0 10px' }, '›'), text({}, '조간'), text({ color: C.accent }, '.'))),
    box({ alignItems: 'baseline', gap: 14, fontFamily: 'Pretendard' },
      text({ fontWeight: 700, fontSize: 26, color: C.accent, letterSpacing: 1 }, kind),
      text({ fontWeight: 600, fontSize: 26, color: C.muted }, when)));

  const main = box({ flexDirection: 'column', gap: 18, flexGrow: 1, justifyContent: 'center' },
    box({ width: 56, height: 5, background: C.accent, borderRadius: 3 }),
    words(headline, { fontFamily: 'Hahmlet', fontWeight: 800, fontSize: headlineSize(headline, term), lineHeight: 1.28, color: '#fff', letterSpacing: -0.5 }),
    sub ? words(sub, { fontFamily: 'Pretendard', fontWeight: 500, fontSize: term ? 30 : 32, lineHeight: 1.5, color: term ? C.text : C.muted }) : null);

  const valueSize = (v: string, n: number) => ([...v].length > 9 ? (n > 3 ? 26 : 30) : (n > 3 ? 32 : 36));
  const tone = (change: string) => (/^[-−]/.test(change) ? C.down : /^\+/.test(change) ? C.up : C.muted);
  const bottom = stats?.length
    ? box({ flexDirection: 'column', gap: 12 },
        asOf ? text({ fontFamily: 'Pretendard', fontWeight: 600, fontSize: 20, color: C.muted }, asOf) : null,
        box({ borderTop: `2px solid ${C.border}`, paddingTop: 22 },
          ...stats.map((s, i) => box({ flexDirection: 'column', flex: 1, minWidth: 0, gap: 4, paddingLeft: i ? 24 : 0, paddingRight: 16, borderLeft: i ? `2px solid ${C.border}` : 'none', fontFamily: 'Pretendard' },
            text({ fontWeight: 600, fontSize: 22, color: C.muted, ...oneLine }, s.label),
            // 숫자는 자르지 않는다. 긴 값("5.163~5.196%")은 글자를 줄이고, 등락은 값 아래 줄에 둔다
            text({ fontWeight: 700, fontSize: valueSize(s.value, stats.length), color: C.text, letterSpacing: -0.3, whiteSpace: 'nowrap' }, s.value),
            s.change ? text({ fontWeight: 700, fontSize: 22, color: tone(s.change) }, s.change.replace(/^-/, '−')) : null,
            s.note ? text({ fontWeight: 500, fontSize: 20, color: C.muted, ...oneLine }, s.note) : null))))
    : box({ justifyContent: 'flex-end', fontFamily: 'Pretendard', fontWeight: 600, fontSize: 22, color: C.muted }, text({}, 'gyeonmunrok.com/jogan/terms'));

  return box({ width: 1200, height: 630, flexDirection: 'column', padding: '52px 68px 50px', gap: 20,
    backgroundColor: C.bg, backgroundImage: `radial-gradient(900px 420px at 18% -12%, ${C.glow} 0%, ${C.bg} 62%)` },
    top, main, bottom);
}

const DAYS = ['일', '월', '화', '수', '목', '금', '토'];
// 글 날짜는 자정(UTC)으로 들어오므로 UTC 기준으로 읽는다
const md = (d: Date) => ({ m: d.getUTCMonth() + 1, d: d.getUTCDate() });
function shortPeriod(p: { from: Date; to: Date }) {
  const a = md(p.from), b = md(p.to);
  return a.m === b.m ? `${a.m}월 ${a.d}~${b.d}일` : `${a.m}월 ${a.d}일~${b.m}월 ${b.d}일`;
}
const afterDash = (title: string) => (title.includes(' — ') ? title.slice(title.indexOf(' — ') + 3) : title);

export function postCard(post: Post): Card | undefined {
  const kind = kindOf(post);
  const d = post.data;
  const highlights = d.highlights?.slice(0, 3);
  if (kind === 'daily') {
    const { m, d: day } = md(d.pubDate);
    const rows = d.front?.markets.rows ?? [];
    const stats = CARD_MARKETS
      .map((name) => rows.find((r) => r.name === name))
      .filter((r): r is NonNullable<typeof r> => Boolean(r && r.value && r.value !== '—'))
      .map((r) => ({ label: r.name, value: r.value, change: r.change }));
    // 기준일은 asOf의 첫 마디다. 휴장한 시장이 있으면 그 마디도 붙인다.
    // 카드의 코스피·원/달러가 미국과 다른 날의 종가일 수 있어서다(10/6: 미국 5일, 국내 2일).
    const segs = (d.front?.markets.asOf ?? '').split(' · ');
    const closed = segs.find((x) => x.includes('휴장'));
    return {
      kind: '일일', when: `${m}월 ${day}일 (${DAYS[d.pubDate.getUTCDay()]})`, headline: headlineOf(post),
      stats, asOf: [segs[0], closed].filter(Boolean).join(' · '),
    };
  }
  if (kind === 'weekly') {
    return { kind: '주간 흐름', when: d.period ? shortPeriod(d.period) : '', headline: afterDash(d.title), stats: highlights };
  }
  if (kind === 'feature') {
    const [head, ...rest] = d.title.split(' — ');
    return { kind: '기획', when: d.period ? shortPeriod(d.period) : '', headline: head, sub: rest.join(' — ') || undefined, stats: highlights };
  }
  return undefined;
}

export function termCard(term: Term): Card {
  // 설명은 두 문장까지(너무 길면 한 문장)
  // 마침표 뒤에 빈칸이 올 때만 자른다("0.20%" 같은 소수점은 그대로)
  const sentences = term.data.description.split(/(?<=[.?!])\s+/);
  const two = sentences.slice(0, 2).join(' ');
  return { kind: '용어', when: term.data.category, headline: term.data.name, sub: [...two].length <= 90 ? two : sentences[0], term: true };
}

export async function renderCard(card: Card) {
  const svg = await satori(layout(card) as Parameters<typeof satori>[0], { width: 1200, height: 630, fonts: FONTS });
  return sharp(Buffer.from(svg)).png().toBuffer();
}
