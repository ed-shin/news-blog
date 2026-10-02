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
  // 오늘 볼 일정(한국 시간). 1면 지표 아래에 나온다. 없는 날은 두지 않는다
  schedule: z
    .array(z.object({ when: z.string(), title: z.string(), prev: z.string().optional(), url: z.string().url() }))
    .max(2)
    .optional(),
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
    // 검색 결과·공유 카드 제목(<title>, og:title)을 따로 줄 때. 글 머리 제목은 그대로다.
    // 사람들이 실제로 검색하는 말이 제목과 다를 때 기획 글에 쓴다(예: "미국 국채 금리 상승의 의미")
    searchTitle: z.string().optional(),
  }).superRefine((data, ctx) => {
    if (data.tags.includes('기획') && !data.period) {
      ctx.addIssue({ code: z.ZodIssueCode.custom, path: ['period'], message: '기획 글은 period: { from, to }로 다루는 기간을 적어야 합니다' });
    }
    if ((data.tags.includes('주간') || data.tags.includes('주간 흐름')) && !data.period) {
      ctx.addIssue({ code: z.ZodIssueCode.custom, path: ['period'], message: '주간 흐름은 period: { from, to }가 있어야 합니다(주소가 from 날짜로 정해짐)' });
    }
  }),
});

// 용어 해설. 한 쪽에 용어 하나. 일일·주간·기획 본문에서 aliases가 처음 나오는 곳에 자동으로 링크가 걸린다
// (astro.config.mjs의 rehypeTermLinks). aliases는 한 줄 배열로 쓴다: aliases: ["장단기 금리차", "금리차"]
const terms = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/terms' }),
  schema: z.object({
    name: z.string(),                 // 목록과 링크에 보이는 이름
    title: z.string(),                // 페이지 제목. 검색하는 모양으로: "장단기 금리차란? 뜻과 역전이 말하는 것"
    description: z.string(),          // 한두 문장. 목록과 검색 결과 설명에 쓰인다
    category: z.enum(['금리', '물가', '경기', '시장', '에너지']),
    aliases: z.array(z.string()).min(1),
    related: z.array(z.string()).default([]),   // 다른 용어 파일 이름(확장자 없이)
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    corrections: z.array(z.object({ date: z.coerce.date(), text: z.string() })).optional(),
  }),
});

export const collections = { blog, terms };
