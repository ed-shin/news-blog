import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// 조간 1면 데이터. 일일 글에만 둔다. 등락(change)은 부호를 붙여 적는다: "+1.37%", "-2.69%", "+0.25%p"
const front = z.object({
  headline: z.string(),
  analysis: z.array(z.object({ lead: z.string(), text: z.string() })).min(1),
  markets: z.object({
    asOf: z.string(),
    rows: z.array(z.object({ name: z.string(), value: z.string(), change: z.string().default('') })),
  }),
  desks: z.array(
    z.object({
      key: z.enum(['rates', 'energy', 'geo', 'tech', 'etc']),
      items: z
        .array(z.object({ title: z.string(), text: z.string(), source: z.string(), url: z.string().url() }))
        .min(1)
        .max(2),
      summary: z.string(),
    })
  ),
});

const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
    front: front.optional(),
    // 글이 다루는 기간. 기획은 필수, 주간 흐름도 적어두면 함께 표시된다
    period: z.object({ from: z.coerce.date(), to: z.coerce.date() }).optional(),
    // 공개 뒤 고친 내역. updatedDate와 함께 쓰고 /jogan/corrections/ 에 모인다
    corrections: z.array(z.object({ date: z.coerce.date(), text: z.string() })).optional(),
    // 흐름 페이지에서 기획·주간 글 아래 숫자 칸으로 보인다 (라벨 / 값 / 메모). 3개 안팎
    highlights: z.array(z.object({ label: z.string(), value: z.string(), note: z.string().optional() })).optional(),
  }).superRefine((data, ctx) => {
    if (data.tags.includes('기획') && !data.period) {
      ctx.addIssue({ code: z.ZodIssueCode.custom, path: ['period'], message: '기획 글은 period: { from, to }로 다루는 기간을 적어야 합니다' });
    }
    if ((data.tags.includes('주간') || data.tags.includes('주간 흐름')) && !data.period) {
      ctx.addIssue({ code: z.ZodIssueCode.custom, path: ['period'], message: '주간 흐름은 period: { from, to }가 있어야 합니다(주소가 from 날짜로 정해짐)' });
    }
  }),
});

export const collections = { blog };
