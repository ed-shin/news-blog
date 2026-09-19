import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import { postUrl } from '../lib/posts';

export async function GET(context) {
  const posts = (await getCollection('blog', ({ data }) => !data.draft)).sort(
    (a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf()
  );
  return rss({
    title: '견문록',
    description: '보고 들은 것을 기록하는 블로그',
    site: context.site,
    items: posts.map((post) => ({
      title: post.data.title,
      description: post.data.description,
      pubDate: post.data.pubDate,
      link: postUrl(post),
    })),
    customData: '<language>ko</language>',
  });
}
