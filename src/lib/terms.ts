import { getCollection, type CollectionEntry } from 'astro:content';
import type { Post } from './posts';

export type Term = CollectionEntry<'terms'>;
export const TERM_CATEGORIES = ['금리', '물가', '경기', '시장', '에너지'] as const;

export async function getTerms() {
  return (await getCollection('terms')).sort((a, b) => a.data.name.localeCompare(b.data.name, 'ko'));
}

export const termUrl = (term: Term) => `/jogan/terms/${term.id}/`;

// 본문에서 이 용어를 쓴 글. 자동 링크(astro.config.mjs)와 같은 기준으로 찾는다:
// 영문 약어는 앞뒤가 영문자가 아닐 때만 인정한다(BEI ≠ BEIJING)
export function mentions(term: Term, posts: Post[]) {
  const tests = term.data.aliases.map((a) =>
    /^[\x20-\x7e]+$/.test(a)
      ? (text: string) => new RegExp(`(?<![A-Za-z])${a.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}(?![A-Za-z])`).test(text)
      : (text: string) => text.includes(a),
  );
  return posts.filter((p) => tests.some((t) => t(p.body ?? '')));
}
