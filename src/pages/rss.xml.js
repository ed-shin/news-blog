import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import { postUrl } from '../lib/posts';
import { termUrl } from '../lib/terms';

// 네이버 서치어드바이저는 새 글을 RSS로 많이 찾고, 본문 전체를 담은 RSS를 권한다.
// 그래서 조간 글과 용어 페이지를 함께 싣고, 본문 HTML을 content:encoded로 넣는다(2026-10-15).
// 본문 속 내부 링크(/jogan/…)는 RSS 리더와 수집기가 따라갈 수 있게 절대 주소로 바꾼다.
const absolutize = (html, origin) => html.replace(/(href|src)="\/(?!\/)/g, `$1="${origin}/`);

export async function GET(context) {
  const origin = new URL(context.site).origin;
  const posts = await getCollection('blog', ({ data }) => !data.draft);
  const terms = await getCollection('terms');
  const items = [
    ...posts.map((post) => ({
      title: post.data.title,
      description: post.data.description,
      pubDate: post.data.pubDate,
      link: postUrl(post),
      categories: post.data.tags,
      content: absolutize(post.rendered?.html ?? '', origin),
    })),
    ...terms.map((term) => ({
      title: term.data.title,
      description: term.data.description,
      pubDate: term.data.pubDate,
      link: termUrl(term),
      categories: ['용어', term.data.category],
      content: absolutize(term.rendered?.html ?? '', origin),
    })),
  ].sort((a, b) => b.pubDate.valueOf() - a.pubDate.valueOf());

  return rss({
    title: '견문록',
    description: '보고 들은 것을 기록하는 블로그',
    site: context.site,
    items,
    customData: '<language>ko</language>',
  });
}
