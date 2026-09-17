import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import remarkGfm from 'remark-gfm';

export default defineConfig({
  site: 'https://gyeonmunrok.com',
  integrations: [sitemap()],
  markdown: {
    // "3.50~3.75%"처럼 범위에 쓰는 물결표가 취소선이 되지 않도록 ~~두 개~~만 취소선으로 인정
    gfm: false,
    remarkPlugins: [[remarkGfm, { singleTilde: false }]],
  },
});
