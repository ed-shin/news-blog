import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import remarkGfm from 'remark-gfm';
import { readdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

// 1면 데스크 이름이 가리키는 브리핑 전문의 섹션 고정 주소 (제목 앞 단어 → id)
const SECTION_IDS = [
  ['3줄 요약', 'summary'], ['오늘의 숫자', 'numbers'], ['금리', 'rates'], ['에너지', 'energy'],
  ['시장', 'market'], ['지정학', 'geo'], ['IT', 'tech'], ['그 외', 'etc'], ['다음에 볼 것', 'next'],
];

// 본문 후처리: "**해설:**"로 시작하는 단락에 .analysis, 표는 가로 스크롤용 .table-wrap으로 감싸고,
// 데스크 섹션 제목에 고정 id, 외부 출처 링크는 새 탭으로 연다.
// "금리 — 연준이 …" 같은 제목은 분야 라벨과 제목으로 나누고, 표의 "+1.37%"·"-2.69%" 칸에 등락 색을 입힌다
function rehypeEditorial() {
  const textOf = (node) =>
    node.type === 'text' ? node.value : (node.children ?? []).map(textOf).join('');
  const span = (className, value) =>
    ({ type: 'element', tagName: 'span', properties: { className: [className] }, children: [{ type: 'text', value }] });

  const visit = (node) => {
    if (!node.children) return;
    node.children = node.children.map((child) => {
      if (child.type !== 'element') return child;
      visit(child);

      if (child.tagName === 'h2') {
        const title = textOf(child).trim();
        const match = SECTION_IDS.find(([prefix]) => title.startsWith(prefix));
        if (match) child.properties = { ...child.properties, id: match[1] };
        const dash = title.indexOf(' — ');
        if (dash > 0 && child.children.every((c) => c.type === 'text')) {
          child.properties = { ...child.properties, className: ['split'] };
          // 가운데 " — "는 화면에서 숨기되 목차·스크린리더용으로 남긴다
          child.children = [span('h-label', title.slice(0, dash)), span('h-sep', ' — '), span('h-title', title.slice(dash + 3))];
        }
      }

      if (child.tagName === 'td') {
        const value = textOf(child).trim();
        if (/^\+\d/.test(value)) child.properties = { ...child.properties, className: ['up'] };
        else if (/^[-−]\d/.test(value)) child.properties = { ...child.properties, className: ['down'] };
      }

      if (child.tagName === 'a' && /^https?:\/\//.test(child.properties?.href ?? '') &&
          !String(child.properties.href).includes('gyeonmunrok.com')) {
        child.properties = { ...child.properties, target: '_blank', rel: ['noopener', 'noreferrer'] };
      }

      if (child.tagName === 'table') {
        return { type: 'element', tagName: 'div', properties: { className: ['table-wrap'] }, children: [child] };
      }

      if (child.tagName === 'p') {
        const first = child.children.find((c) => !(c.type === 'text' && !c.value.trim()));
        if (first?.type === 'element' && first.tagName === 'strong' && /^(해설|분석)\s*:?$/.test(textOf(first).trim())) {
          child.properties = { ...child.properties, className: ['analysis'] };
          first.properties = { ...first.properties, className: ['analysis-label'] };
          first.children = [{ type: 'text', value: '해설' }];
        }
      }
      return child;
    });
  };

  return (tree) => visit(tree);
}

// 용어 파일을 읽는다. 자동 링크와 사이트맵 갱신일에 쓴다
function loadTerms() {
  const dir = 'src/content/terms';
  let files = [];
  try { files = readdirSync(dir).filter((f) => f.endsWith('.md')); } catch { return []; }
  return files.map((name) => {
    const fm = readFileSync(join(dir, name), 'utf8').split('---')[1] ?? '';
    const field = (key) => fm.match(new RegExp(`^${key}:\\s*(\\S+)`, 'm'))?.[1];
    const aliases = JSON.parse(fm.match(/^aliases:\s*(\[.*\])\s*$/m)?.[1] ?? '[]');
    return { slug: name.replace(/\.md$/, ''), aliases, date: field('updatedDate') ?? field('pubDate') ?? '' };
  });
}
const TERMS = loadTerms();

// 본문에서 용어가 처음 나오는 곳에 용어 페이지 링크를 건다. 글마다 용어 하나에 한 번만.
// 제목·링크·인용·표·차트·코드 안은 건드리지 않는다. 영문 약어는 앞뒤가 영문자가 아닐 때만 잡는다(BEI ≠ BEIJING).
// 같은 자리에서 여럿이 걸리면 긴 말이 이긴다("근원 PCE" > "PCE").
function rehypeTermLinks() {
  const list = TERMS.flatMap((t) => t.aliases.map((a) => ({ a, slug: t.slug })))
    .sort((x, y) => y.a.length - x.a.length)
    .map((x) => ({ ...x, re: /^[\x20-\x7e]+$/.test(x.a)
      ? new RegExp(`(?<![A-Za-z])${x.a.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}(?![A-Za-z])`)
      : null }));
  const SKIP = new Set(['a', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'code', 'pre', 'table', 'figure', 'svg', 'blockquote', 'script', 'style']);
  return (tree, file) => {
    const path = String(file?.path ?? file?.history?.[0] ?? '');
    if (!path.includes('/content/blog/')) return;   // 용어 페이지 자신과 그 밖의 페이지는 건드리지 않는다
    const done = new Set();
    const linkText = (text) => {
      let best = null;
      for (const x of list) {
        if (done.has(x.slug)) continue;
        const i = x.re ? (text.match(x.re)?.index ?? -1) : text.indexOf(x.a);
        if (i >= 0 && (!best || i < best.i)) best = { i, ...x };
      }
      if (!best) return [{ type: 'text', value: text }];
      done.add(best.slug);
      const link = { type: 'element', tagName: 'a', properties: { href: `/jogan/terms/${best.slug}/`, className: ['term'] },
        children: [{ type: 'text', value: best.a }] };
      const before = text.slice(0, best.i);
      return [...(before ? [{ type: 'text', value: before }] : []), link, ...linkText(text.slice(best.i + best.a.length))];
    };
    const walk = (node) => {
      if (!node.children) return;
      node.children = node.children.flatMap((c) => {
        if (c.type === 'text') return linkText(c.value);
        if (c.type === 'element' && !SKIP.has(c.tagName)) walk(c);
        return [c];
      });
    };
    walk(tree);
  };
}

// 사이트맵의 lastmod — 글 파일에서 발행일(수정일이 있으면 수정일)을 읽어 주소별로 모은다.
// 검색엔진이 사이트맵만 보고도 무엇이 새로 생겼는지 알 수 있게 하는 값이다.
// 주소 규칙은 src/lib/posts.ts의 postUrl과 같게 유지해야 한다. 어긋나면 그 글만 lastmod 없이 나간다.
function postLastmod() {
  const dir = 'src/content/blog';
  const map = new Map();
  let newest = '';
  for (const name of readdirSync(dir).filter((f) => f.endsWith('.md'))) {
    const fm = readFileSync(join(dir, name), 'utf8').split('---')[1] ?? '';
    const field = (key) => fm.match(new RegExp(`^${key}:\\s*(\\S+)`, 'm'))?.[1];
    const pubDate = field('pubDate');
    if (!pubDate) continue;
    const last = field('updatedDate') ?? pubDate;
    const tags = fm.match(/^tags:\s*\[(.*)\]/m)?.[1] ?? '';
    const slug = name.replace(/\.md$/, '');

    if (tags.includes('일일')) {
      map.set(`/jogan/daily/${pubDate}/`, last);
    } else if (tags.includes('주간')) {
      // period는 { from: 2026-09-14, to: ... } 한 줄 형식이라 날짜만 끊어 읽는다
      map.set(`/jogan/weekly/${fm.match(/from:\s*([\d-]+)/)?.[1] ?? pubDate}/`, last);
    } else if (tags.includes('기획')) {
      map.set(`/jogan/feature/${slug.replace(/^\d{4}-\d{2}-\d{2}-/, '')}/`, last);
    } else {
      map.set(`/blog/${slug}/`, last);
    }
    if (last > newest) newest = last;
  }
  // 새 글이 올라오면 함께 바뀌는 페이지들
  for (const url of ['/', '/jogan/', '/jogan/all/', '/jogan/flow/', '/jogan/terms/']) map.set(url, newest);
  // 용어 페이지의 "요즘 나온 글"은 그 용어를 쓴 새 글이 올라올 때 바뀐다
  for (const t of TERMS) {
    let last = t.date;
    for (const name of readdirSync(dir).filter((f) => f.endsWith('.md'))) {
      const text = readFileSync(join(dir, name), 'utf8');
      const pub = text.split('---')[1]?.match(/^pubDate:\s*(\S+)/m)?.[1] ?? '';
      if (pub > last && t.aliases.some((a) => text.split('---').slice(2).join('---').includes(a))) last = pub;
    }
    map.set(`/jogan/terms/${t.slug}/`, last);
  }
  return map;
}

const lastmod = postLastmod();

export default defineConfig({
  site: 'https://gyeonmunrok.com',
  integrations: [
    sitemap({
      // 날짜별 1면(/jogan/today/날짜/)은 같은 날 일일 글과 내용이 겹쳐
      // 검색엔진이 색인하지 않는다. 사람이 보는 페이지로만 두고 사이트맵에서 뺀다.
      filter: (page) => !new URL(page).pathname.startsWith('/jogan/today/'),
      serialize(item) {
        const date = lastmod.get(new URL(item.url).pathname);
        if (date) item.lastmod = date;
        return item;
      },
    }),
  ],
  markdown: {
    // "3.50~3.75%"처럼 범위에 쓰는 물결표가 취소선이 되지 않도록 ~~두 개~~만 취소선으로 인정
    gfm: false,
    remarkPlugins: [[remarkGfm, { singleTilde: false }]],
    rehypePlugins: [rehypeEditorial, rehypeTermLinks],
  },
});
