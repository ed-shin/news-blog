import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import remarkGfm from 'remark-gfm';

// 1면 데스크 이름이 가리키는 브리핑 전문의 섹션 고정 주소 (제목 앞 단어 → id)
const SECTION_IDS = [
  ['3줄 요약', 'summary'], ['오늘의 숫자', 'numbers'], ['금리', 'rates'], ['에너지', 'energy'],
  ['시장', 'market'], ['지정학', 'geo'], ['IT', 'tech'], ['그 외', 'etc'],
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

export default defineConfig({
  site: 'https://gyeonmunrok.com',
  integrations: [sitemap()],
  markdown: {
    // "3.50~3.75%"처럼 범위에 쓰는 물결표가 취소선이 되지 않도록 ~~두 개~~만 취소선으로 인정
    gfm: false,
    remarkPlugins: [[remarkGfm, { singleTilde: false }]],
    rehypePlugins: [rehypeEditorial],
  },
});
