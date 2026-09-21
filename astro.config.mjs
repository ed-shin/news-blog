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
      map.set(`/jogan/today/${pubDate}/`, last); // 그날의 1면도 같은 글에서 나온다
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
  for (const url of ['/', '/jogan/', '/jogan/all/', '/jogan/flow/']) map.set(url, newest);
  return map;
}

const lastmod = postLastmod();

export default defineConfig({
  site: 'https://gyeonmunrok.com',
  integrations: [
    sitemap({
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
    rehypePlugins: [rehypeEditorial],
  },
});
