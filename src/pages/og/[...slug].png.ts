// 글·용어마다 대표 이미지를 빌드 때 만든다. /jogan/daily/2026-09-30/ → /og/jogan/daily/2026-09-30.png
// 카드 모양과 무엇을 싣는지는 src/lib/og.ts에 있다.
import type { APIRoute, GetStaticPaths } from 'astro';
import { getJoganPosts, postUrl, ogImagePath } from '../../lib/posts';
import { getTerms, termUrl } from '../../lib/terms';
import { postCard, termCard, renderCard } from '../../lib/og';

export const getStaticPaths: GetStaticPaths = async () => {
  const slug = (pagePath: string) => ogImagePath(pagePath).replace(/^\/og\//, '').replace(/\.png$/, '');
  const posts = (await getJoganPosts()).flatMap((post) => {
    const card = postCard(post);
    return card ? [{ params: { slug: slug(postUrl(post)) }, props: { card } }] : [];
  });
  const terms = (await getTerms()).map((term) => ({ params: { slug: slug(termUrl(term)) }, props: { card: termCard(term) } }));
  return [...posts, ...terms];
};

export const GET: APIRoute = async ({ props }) => {
  const png = await renderCard(props.card);
  return new Response(new Uint8Array(png), { headers: { 'Content-Type': 'image/png' } });
};
