import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// site는 도메인 확정 후 실제 주소로 교체
export default defineConfig({
  site: 'https://gyeonmunrok.com',
  integrations: [sitemap()],
});
