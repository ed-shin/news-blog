import { getCollection, type CollectionEntry } from 'astro:content';

export type Post = CollectionEntry<'blog'>;
export type Kind = 'daily' | 'weekly' | 'feature';

// 조간 글은 tags에 종류 태그 하나를 넣는다. 나머지 태그는 주제.
const KIND_TAGS: Record<string, Kind> = { 일일: 'daily', 주간: 'weekly', '주간 흐름': 'weekly', 기획: 'feature' };
export const KIND_LABEL: Record<Kind, string> = { daily: '일일', weekly: '주간 흐름', feature: '기획' };
export const KINDS = Object.keys(KIND_LABEL) as Kind[];

export const DESK_NAME = { rates: '금리 · 시장', energy: '에너지', geo: '지정학', tech: 'IT · 테크', etc: '그 외' } as const;
const TOPIC_LABEL: Record<string, string> = { 테크: 'IT · 테크' };

export const kindOf = (post: Post): Kind | undefined => post.data.tags.map((t) => KIND_TAGS[t]).find(Boolean);
export const topicsOf = (post: Post) => post.data.tags.filter((t) => !KIND_TAGS[t]);
export const topicLabel = (tag: string) => TOPIC_LABEL[tag] ?? tag;
export const postUrl = (post: Post) => `/blog/${post.id}/`;
export const headlineOf = (post: Post) => post.data.front?.headline ?? post.data.title;

export async function getPosts() {
  const posts = await getCollection('blog', ({ data }) => !data.draft);
  return posts.sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());
}

export async function getJoganPosts() {
  return (await getPosts()).filter((post) => kindOf(post));
}

// ── 날짜: 날짜만 적은 frontmatter(UTC 자정)를 서울 날짜로 읽는다 ──
const WEEKDAYS = ['일', '월', '화', '수', '목', '금', '토'];
function seoul(date: Date) {
  const s = new Date(date.getTime() + 9 * 3600 * 1000);
  return { y: s.getUTCFullYear(), m: s.getUTCMonth() + 1, d: s.getUTCDate(), w: WEEKDAYS[s.getUTCDay()] };
}
export const fmtFull = (date: Date) => { const t = seoul(date); return `${t.y}년 ${t.m}월 ${t.d}일 ${t.w}요일`; };
export const fmtMonthDay = (date: Date) => { const t = seoul(date); return `${t.m}월 ${t.d}일`; };
export const fmtWeekday = (date: Date) => `${seoul(date).w}요일`;
export const fmtShort = (date: Date) => { const t = seoul(date); return { md: `${t.m}.${t.d}`, slash: `${t.m}/${t.d}`, w: t.w }; };
export const fmtMonth = (date: Date) => { const t = seoul(date); return `${t.y}년 ${t.m}월`; };
export const isoDate = (date: Date) => date.toISOString().slice(0, 10);
// "8월 24일 ~ 9월 13일" (해를 넘기면 연도를 붙인다)
export function fmtPeriod(period?: { from: Date; to: Date }) {
  if (!period) return '';
  const a = seoul(period.from);
  const b = seoul(period.to);
  return a.y === b.y
    ? `${a.m}월 ${a.d}일 ~ ${b.m}월 ${b.d}일`
    : `${a.y}년 ${a.m}월 ${a.d}일 ~ ${b.y}년 ${b.m}월 ${b.d}일`;
}

// "+1.37%" → 오름, "-2.69%" → 내림, 그 밖은 보합·해당 없음
export function direction(change: string) {
  const sign = change.trim()[0];
  if (sign === '+') return { cls: 'up', arrow: '▲', abs: change.trim().slice(1) };
  if (sign === '-' || sign === '−') return { cls: 'down', arrow: '▼', abs: change.trim().slice(1) };
  return { cls: '', arrow: '', abs: change.trim() };
}

export const firstSentence = (text: string) => text.match(/^.*?\.(?=\s|$)/)?.[0] ?? text;
