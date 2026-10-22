---
title: "OpenAI·Anthropic·Google 9~10월 새 모델 출시"
description: "9월 1일부터 10월 13일 사이 OpenAI, Anthropic, Google이 새 AI 모델을 잇달아 냈다. GPT-6 Astra와 GPT-6.1 Sol, Claude Fable 5.1과 Opus 5.5, Gemini 4 Argon을 중심으로 출시 순서, 값, 쓸 수 있는 곳, 회사가 내세운 점을 정리하고, 회사가 아닌 외부 기관의 평가를 측정 조건과 함께 모았다."
pubDate: 2026-10-23
tags: ["기획", "테크"]
searchTitle: "2026년 9~10월 AI 모델 출시 — GPT-6 Astra·Claude Fable 5.1·Gemini 4 Argon | 견문록"
period: { from: 2026-09-01, to: 2026-10-13 }
highlights:
  - { label: "주요 새 모델", value: "5개", note: "Astra·Sol·Fable·Opus·Argon" }
  - { label: "가장 비싼 등급", value: "$10 / $50", note: "Astra·Fable 5.1, 100만 토큰당" }
  - { label: "외부 평가", value: "3곳", note: "Artificial Analysis·Vals·ARC Prize" }
---

## 먼저 요점만

1. **9월 1일부터 10월 13일 사이, 세 회사가 주요 모델을 새로 냈다.** Anthropic이 Claude Fable 5.1과 Opus 5.5를, OpenAI가 GPT-6 Astra와 GPT-6.1 Sol을 냈다. Google의 Gemini 4 Argon은 9월 30일 일부에게 먼저 풀린 뒤 10월 13일 API로 전 세계에 공개됐다.
2. **값은 크게 두 층으로 나뉜다.** Astra와 Fable 5.1이 가장 비싸고, Opus 5.5는 그 5분의 2, Sol과 Argon은 5분의 1 값이다. 다만 Argon은 도입가여서 12월부터 두 배로 오른다.
3. **외부 평가 점수는 측정 조건과 함께 봐야 한다.** 같은 평가에서도 추론 설정과 평가판에 따라 숫자가 바뀐다. 특히 Anthropic 모델의 점수 일부에는 거절된 요청을 다른 모델이 대신 푼 몫('폴백')이 섞여 있다.

9월 20일~10월 12일 일곱 회사의 새 모델은 [AI 모델 3주](/jogan/feature/ai-models-three-weeks/)에 정리했다. 이 글은 그 가운데 세 회사가 9~10월 낸 범용 모델만 다루고, 음성·이미지 전용 모델은 뺐다.

## 출시 순서

**6주 사이 세 회사가 모델 열한 개를 냈다.** 아래 값은 앱 구독료가 아니라 API 사용료인데, API는 다른 프로그램에서 모델을 불러 쓰는 연결 방식이고 토큰은 AI가 글을 읽고 쓰는 단위다. 용도에 나오는 에이전트 작업은 AI가 도구를 써서 여러 단계를 스스로 해내는 일을 말한다. 굵은 글씨는 주요 모델이다.

| 발표(현지) | 회사 | 모델 | 100만 토큰당 값(입력/출력) | 용도(회사 설명) |
|---|---|---|---|---|
| 9월 1일 | Anthropic | **Claude Fable 5.1** | $10 / $50 | 어려운 문제 풀이, 오래 걸리는 에이전트 작업 |
| 9월 2일 | Google | Gemini 3.8 Flash | $0.75 / $3.75(12월까지) | 일상 업무를 맡는 주력(workhorse) 모델 |
| 9월 2일 | Google | Gemini 3.8 Flash Cyber | 공개 안 함 | 취약점 탐지, 검증된 방어자에게만 제공 |
| 9월 3일 | OpenAI | **GPT-6 Astra** | $10 / $50 | 가장 까다로운 작업 |
| 9월 22일 | Anthropic | **Claude Opus 5.5** | $4 / $20 | 오래 걸리는 에이전트 코딩, 지식 업무 |
| 9월 22일 | OpenAI | GPT-6 Sol / GPT-6 Luna | $2 / $10, $0.10 / $0.50 | Astra보다 빠르고 싼 모델 |
| 9월 28일 | Anthropic | Claude Sonnet 5.5 | $2 / $10 | 속도와 지능의 균형 |
| 9월 29일 | OpenAI | **GPT-6.1 Sol** | $2 / $10 | GPT-6 Sol의 개선판 |
| 9월 30일 | Google | **Gemini 4 Argon** | $2 / $10(12월부터 $4 / $20) | Google의 대표(flagship) 추론 모델, 10월 13일 API 전체 공개 |
| 10월 7일 | Anthropic | Claude Haiku 5.5 | $0.10 / $0.50(입력 10만 토큰 넘으면 $0.50 / $2.50) | 분류·추출처럼 양이 많고 빨라야 하는 작업 |

*회사 설명은 각 회사의 표현을 옮긴 것이다. 출처: [Fable 5.1](https://platform.claude.com/docs/en/models/fable-5-1/overview), [Gemini 3.8 Flash·Flash Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/)·[값](https://ai.google.dev/gemini-api/docs/pricing), [Astra](https://developers.openai.com/api/docs/models/gpt-6-astra), [Opus 5.5](https://platform.claude.com/docs/en/models/opus-5-5/overview), [Sol·Luna](https://x.com/OpenAI/status/2102460975790137662)·[Luna 값](https://developers.openai.com/api/docs/models/gpt-6-luna), [Sonnet 5.5](https://platform.claude.com/docs/en/models/sonnet-5-5/overview), [GPT-6.1 Sol](https://x.com/OpenAI/status/2104986133004505373), [Argon](https://ai.google.dev/gemini-api/docs/models)·[10월 13일](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/), [Haiku 5.5](https://platform.claude.com/docs/en/models/haiku-5-5/overview).*

## 회사별 모델

### OpenAI

**OpenAI는 9월 3일 GPT-6 Astra를 내고, 그 아래 등급을 두 번 새로 냈다.** Astra는 [OpenAI](https://x.com/OpenAI/status/2095595742975197690)가 컴퓨터 조작, 웹 탐색, 소프트웨어 개발, 사이버보안, 과학, 전문 업무용으로 내세운 모델이다. 22일에는 그 강점을 더 빠르고 싼 모델에 담았다는 [GPT-6 Sol과 Luna](https://x.com/OpenAI/status/2102460975790137662)가 나왔고, 일주일 뒤에는 코딩과 컴퓨터 조작, 복잡한 전문 업무를 개선한 [GPT-6.1 Sol](https://x.com/OpenAI/status/2104986133004505373)이 나왔다.

Astra는 [출시 당일](https://x.com/OpenAI/status/2095595757072191802) 일부 기관에 먼저 풀린 뒤, [이튿날](https://x.com/OpenAI/status/2095968413646737608)인 9월 4일부터 ChatGPT Pro·Enterprise·Business Premium 이용자도 ChatGPT Work와 Codex, API에서 쓸 수 있게 됐다. 9월 29일부터는 [GPT-6.1 Sol](https://x.com/OpenAI/status/2104986136745767160)도 유료 요금제의 ChatGPT Work와 Codex, 그리고 API에서 쓸 수 있고, 10월 7일에는 [일반 ChatGPT 대화](https://deploymentsafety.openai.com/gpt-6-october)에도 GPT-6 Sol과 Luna가 무료·유료 구분 없이 들어갔다.

### Anthropic

**Anthropic은 9월 1일 Claude Fable 5.1을 낸 뒤 Opus·Sonnet·Haiku 5.5를 차례로 내놨다.** [Fable 5.1](https://platform.claude.com/docs/en/models/fable-5-1/overview)은 오래 걸리는 에이전트 코딩, 여러 단계의 조사, 문서·스프레드시트·슬라이드 작업을 개선했다고 내세운 모델이고, 그 아래 [Opus 5.5](https://www.anthropic.com/claude-opus-5-5)는 대부분의 일에서 Fable 5.1 수준이라는 것이 회사의 주장이다. Fable 5.1과 같은 성능의 Claude Mythos 5.1은 Anthropic의 [검증 프로그램](https://platform.claude.com/docs/en/models/fable-5-1/overview)을 거친 기관에만 준다.

Fable 5.1과 Opus 5.5는 [Claude 앱 유료 요금제](https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans)와 Claude Code에서 쓸 수 있지만, Pro 요금제나 Team의 표준 계정에서 Fable 5.1을 쓰려면 [별도 사용 크레딧](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan)이 필요하다. API와 AWS·Google Cloud·Microsoft에서는 [네 모델을 모두](https://platform.claude.com/docs/en/models/fable-5-1/overview) 쓸 수 있다.

### Google

**Google은 9월 2일 Gemini 3.8 Flash와 Flash Cyber를, 9월 30일 Gemini 4 Argon을 냈다.** 이 가운데 [Flash Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/)는 취약점 탐지용이라 사이버 방어 프로그램 'Fairwind'의 검증된 방어자에게만 준다. Argon은 [코딩, 기업 지식 업무, 사이버 방어](https://x.com/GoogleDeepMind/status/2105388084154056939)를 위해 만든 모델로, 중대한 소프트웨어 취약점을 스스로 찾고 검증하고 고칠 수 있다는 것이 [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)의 설명이다.

Argon도 처음에는 Fairwind 참여자에게만 풀렸다가 [10월 13일](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/) API로 전 세계에 공개됐고, Gemini 앱과 검색 AI 모드(AI Pro·Ultra 구독자), Antigravity(AI Ultra)에서도 쓸 수 있다.

## 주요 모델 다섯

**다섯 모델은 한 번에 담을 수 있는 글의 양이 비슷하다.** 차이는 값과 넣을 수 있는 자료에서 나는데, Argon만 영상과 음성까지 받는다. 다섯 모두 모델의 내부 값(가중치)을 공개하지 않아 내려받아 직접 돌릴 수는 없다. 아래 표의 값은 100만 토큰당 입력/출력 API 사용료이고, 문맥 한도는 한 요청에 담는 입력과 출력을 합친 양, 최대 출력은 한 번에 내놓을 수 있는 답의 양이다. 단위는 모두 토큰이다.

| 모델 | 값(입력/출력) | 문맥 한도 | 최대 출력 | 넣을 수 있는 것 | 지식 기준 |
|---|---|---|---|---|---|
| GPT-6 Astra | $10 / $50 | 105만 | 12만 8,000 | 글·이미지 | 2026년 4월 30일 |
| GPT-6.1 Sol | $2 / $10 | 105만 | 12만 8,000 | 글·이미지 | 2026년 4월 30일 |
| Claude Fable 5.1 | $10 / $50 | 100만 | 12만 8,000 | 글·이미지 | 2026년 6월 |
| Claude Opus 5.5 | $4 / $20 | 100만 | 12만 8,000 | 글·이미지 | 2026년 6월 |
| Gemini 4 Argon | $2 / $10 | 약 105만 | 6만 5,536 | 글·이미지·영상·음성 | 2026년 3월 |

*Argon은 12월부터 $4 / $20이고, 긴 출력 기능을 쓰면 약 105만 토큰까지 내놓는다. OpenAI 두 모델은 입력이 27만 2,000토큰을 넘으면 그 요청 전체에 입력 2배·출력 1.5배 값을 받는다. 출처: [Astra](https://developers.openai.com/api/docs/models/gpt-6-astra), [Sol](https://developers.openai.com/api/docs/models/gpt-6.1-sol), [Fable 5.1](https://platform.claude.com/docs/en/models/fable-5-1/overview), [Opus 5.5](https://platform.claude.com/docs/en/models/opus-5-5/overview), [Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon)·[모델 카드](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Argon-Model-Card.pdf).*

## 외부 평가

**모델을 고를 때는 하려는 일과 닮은 평가를 찾아, 그 일에 드는 값과 함께 보는 편이 낫다.** 아래는 회사가 아닌 Artificial Analysis, Vals, ARC Prize가 직접 잰 결과다.

| 모델 | Artificial Analysis 지능 지수 | Vals 지수 2.2판 | ARC-AGI-2 |
|---|---|---|---|
| GPT-6 Astra | 53 | 65.02% ±1.10 | 95.0% |
| GPT-6.1 Sol | 52 | 63.94% ±1.07 | 94.2% |
| Claude Fable 5.1 | 53(기본 폴백 켬) | — | 90.0% |
| Claude Opus 5.5 | 58(기본 폴백 켬) | 70.18% ±1.00(폴백 과제를 실패로 치면 64.16%) | 93.3% |
| Gemini 4 Argon | 53 | 69.24% ±1.09 | 91.3% |

- **Artificial Analysis:** 어려운 지식 문제, 과학 코딩, 에이전트 과제 등 10개 평가를 묶은 점수다. 9월 7일 평가 구성을 바꾼 판 기준이고, Argon만 가장 높은 설정이 high여서 high로, 나머지는 max로 쟀다. Astra·Fable 5.1은 9월 9일, Opus 5.5는 9월 22일, Sol·Argon은 9월 30일 발표([Astra·Fable 5.1](https://artificialanalysis.ai/articles/benchmarking-gpt-6-astra), [Opus 5.5](https://x.com/ArtificialAnlys/status/2102438210798514391), [Sol·Argon](https://x.com/ArtificialAnlys/status/2105392625788637299)).
- **Vals:** 금융·코딩·법률·세무 업무에서 AI가 여러 단계를 해내는 능력을 재고, 미국 경제에서 각 분야가 차지하는 비중대로 점수를 합친다(금융과 코딩이 약 90%). 10월 19일 2.2판이고 Fable 5.1은 이 판에 없다. Astra·Sol·Opus 5.5는 max, Argon은 high 설정이다. ±는 표준오차다([Vals](https://web.archive.org/web/20261021142413/https://www.vals.ai/benchmarks/vals_index), [Astra](https://www.vals.ai/models/openai_gpt-6-astra)·[Sol](https://www.vals.ai/models/openai_gpt-6.1-sol)·[Opus 5.5](https://www.vals.ai/models/anthropic_claude-opus-5-5)·[Argon](https://www.vals.ai/models/google_gemini-4-argon)).
- **ARC-AGI-2:** 처음 보는 퍼즐의 규칙을 찾아내는 시험이다. ARC Prize가 비공개 시험 세트(Semi-Private)로 검증한 각 모델의 최고점이고, Astra·Sol·Fable 5.1은 max, Opus 5.5·Argon은 high 설정 점수다. 결과는 9월 1일(Fable 5.1)부터 10월 13일(Argon) 사이에 올라왔다([Astra](https://arcprize.org/results/openai-gpt-6-astra), [Sol](https://arcprize.org/results/openai-gpt-6-1-sol), [Fable 5.1](https://arcprize.org/results/anthropic-claude-fable-5-1), [Opus 5.5](https://arcprize.org/results/anthropic-claude-opus-5-5), [Argon](https://arcprize.org/results/google-gemini-4-argon)).

표의 숫자는 어떤 조건에서 쟀는지와 함께 읽어야 한다. 이 모델들은 답하기 전에 얼마나 오래 생각할지 단계를 고를 수 있는데, ARC Prize 결과를 보면 [Astra](https://arcprize.org/results/openai-gpt-6-astra)는 가장 높은 max에서 95.0%, high에서 92.1%를 냈고, [Opus 5.5](https://arcprize.org/results/anthropic-claude-opus-5-5)는 오히려 high에서 93.3%로 max(91.7%)보다 높았다.

Anthropic 모델은 한 가지 조건을 더 봐야 한다. 안전 분류기가 거절한 요청을 [다른 Claude 모델이 대신 풀게 할 수 있어서](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback), 이 기능(폴백)을 켠 채 잰 점수에는 다른 모델의 몫이 섞인다. Artificial Analysis가 Fable 5.1과 Opus 5.5를 이렇게 쟀고, [Vals](https://www.vals.ai/models/anthropic_claude-opus-5-5)에서는 Opus 5.5가 거절한 과제 4.28%를 Opus 5와 Opus 4.8이 대신 풀었다. 그 과제를 실패로 치면 Opus 5.5의 점수는 70.18%에서 64.16%로 내려가는데, Argon은 [폴백 없이](https://web.archive.org/web/20261021142413/https://www.vals.ai/benchmarks/vals_index) 잰 점수다.

평가판이 바뀌면 숫자도 바로 이어지지 않는다. Artificial Analysis가 9월 7일 평가 구성을 바꾸기 전에는 Fable 5.1 점수가 [66](https://x.com/ArtificialAnlys/status/2094881171066978525)이었고, Vals가 10월 19일 평가 일부와 세무 채점법을 바꾼 2.2판을 내기 하루 전 [2.1판](https://www.vals.ai/benchmarks/vals_index_v2_1)에서는 Argon(68.90%)이 Opus 5.5(66.97%)보다 높았다.

[Vals](https://web.archive.org/web/20261021142413/https://www.vals.ai/benchmarks/vals_index) 지수 시험을 한 번 치르는 데 든 값도 모델마다 크게 달라서, Sol 3.61달러, Argon 13.37달러(정가 기준), Astra 21.28달러, Opus 5.5 28.12달러였다.

## 다음에 볼 것

- **12월 1일 Argon의 도입가가 끝난 뒤.**
  Argon은 11월 30일까지 100만 토큰당 입력 2달러·출력 10달러이고, 12월 1일부터 입력 4달러·출력 20달러다.
  Argon을 API로 쓴다면 12월 1일 Google 가격표와 외부 평가의 시험당 비용이 바뀌는지 보면 된다.
  값이 두 배가 되면 Argon의 토큰당 값은 Opus 5.5와 같아지고, GPT-6.1 Sol의 두 배가 된다.
- **Vals 2.2판에 Fable 5.1이 오르는지.**
  Fable 5.1은 2.1판까지 있었지만 10월 19일 2.2판 목록에는 없다.
  다섯 모델의 Vals 점수를 같은 판으로 견주려면 Vals 지수 페이지에 Fable 5.1이 다시 오르는지 보면 된다.
  오르면 주요 모델 다섯을 같은 판의 Vals 점수로 나란히 놓을 수 있다.
