---
title: "AI 모델 출시 — 11월 10~25일"
description: "11월 10일부터 25일까지 Google, OpenAI, Microsoft, Thinking Machines가 새 AI 모델 일곱을 냈다. Gemini 4 Hydrogen·Neon, GPT-6.2 Astra·Sol, MAI Code 2·Code 2 Flash, Inkling 2 Mini를 발표일·쓸 수 있는 곳·값·가중치 공개 여부로 나란히 놓고, 유료 개발자에게 풀린 Gemini 4 Carbon과 회사가 밝힌 위험 판정, 외부 기관의 평가를 측정 조건과 함께 정리했다."
pubDate: 2026-11-26
tags: ["기획", "테크"]
period: { from: 2026-11-10, to: 2026-11-25 }
highlights:
  - { label: "다룬 새 모델", value: "7개", note: "네 회사, 11/12~11/20 발표" }
  - { label: "100만 토큰당 출력 값", value: "$0.50~$40", note: "Tinker·각 회사 API" }
  - { label: "가중치 공개", value: "2개", note: "Inkling 2 Small·Mini, Apache 2.0" }
---

## 먼저 요점만

1. **11월 12일부터 20일 사이 네 회사가 새 모델 일곱을 냈다.** Google의 Gemini 4 Hydrogen과 Neon, OpenAI의 GPT-6.2 Astra와 Sol, Microsoft의 MAI Code 2와 Code 2 Flash, Thinking Machines의 Inkling 2 Mini이고, 100만 토큰당 출력 값은 Inkling 2 Mini의 0.50달러부터 Astra의 40달러까지다. 일부 사이버 방어자만 쓰던 Gemini 4 Carbon도 10일 돈을 내는 개발자 모두에게 풀렸다.
2. **Thinking Machines는 두 모델의 가중치를 Apache 2.0으로 풀었다.** 앞 편에서 공개를 기다리던 Inkling 2 Small이 12일 허깅페이스에 올라왔고, 20일 낸 Inkling 2 Mini는 처음부터 가중치를 공개했다. Google·OpenAI·Microsoft의 새 모델은 가중치를 공개하지 않았다.
3. **회사가 밝힌 위험 판정은 모델마다 다르다.** OpenAI는 GPT-6.2 두 모델을 사이버보안 Critical, 생물·화학 High로 다룬다. Google은 Hydrogen이 자체 위험 기준에 못 미친다고 봤지만, Neon과 Carbon에는 그 기준에 이르렀을 가능성을 배제할 수 없다는 Argon의 판정을 이어 썼다.

10월 28일~11월 9일에 나온 모델은 [AI 모델 출시 — 10월 28일~11월 9일](/jogan/feature/ai-models-early-november/)에 정리했다. 이 글은 그 뒤 조간 일일 글에 실린 새 모델 일곱을 같은 항목으로 다루고, 앞 편에서 다룬 Carbon과 Inkling 2 Small은 새로 바뀐 것만 적었다. 문서 추출용인 Cloudflare의 Clairic([11월 20일 일일](/jogan/daily/2026-11-20/#tech))과 Microsoft 보안 제품에만 들어가는 MAI Cyber 2 Flash, 음성 모델 MAI Realtime 1은 뺐다.

## 한눈에 보는 여덟 모델

**새 모델 일곱은 값과 가중치 공개에서 갈린다.** 가중치가 공개된 것은 Inkling 2 Mini 하나이고, 나머지 여섯은 회사 서비스와 API로만 쓴다. 값은 앱 구독료가 아니라 다른 프로그램에서 모델을 불러 쓰는 API의 사용료이고, 같은 입력을 반복해 보내면 더 낮은 캐시 값을 받으므로 표에는 캐시되지 않은 입력 값을 적었다. Carbon은 일반 공개 날짜로 함께 넣었고, 위험 판정 칸에는 회사가 자체 기준으로 내놓은 것만 적었다.

| 발표(현지) | 회사 | 모델 | 쓸 수 있는 곳 | 100만 토큰당 값(캐시 안 된 입력/출력) | 가중치 | 회사가 밝힌 위험 판정 |
|---|---|---|---|---|---|---|
| 11월 10일(일반 공개) | Google | Gemini 4 Carbon | Gemini API 유료 등급·Gemini for business, AI Ultra 구독자(Gemini 앱·검색 AI 모드·Antigravity) | $2 / $10(11월 30일까지, 12월 1일부터 $4 / $20) | 비공개 | Argon 판정을 이어받음(사이버·생물 위험 기준 도달 가능성 배제 못 함) |
| 11월 12일 | Google | Gemini 4 Hydrogen | Gemini API(무료 등급 있음)·Gemini for business, Gemini 앱, 구글 검색, Antigravity(AI Pro·Ultra) | $1.50 / $7.50 | 비공개 | 사이버·화생방(CBRN) 위험 기준 미달, 그 경보 기준에는 이름 |
| 11월 17일 | OpenAI | GPT-6.2 Astra | ChatGPT Work·Codex(Plus·Pro·Enterprise·Edu), API | $8 / $40 | 비공개 | 사이버보안 Critical, 생물·화학 High, AI 자기 개선 High |
| 11월 17일 | OpenAI | GPT-6.2 Sol | ChatGPT Work·Codex(Plus·Pro·Enterprise·Edu), API | $2 / $10 | 비공개 | 사이버보안 Critical, 생물·화학 High |
| 11월 17일 | Microsoft | MAI Code 2 / MAI Code 2 Flash | GitHub Copilot, Code 2 Flash는 Microsoft Foundry 제한 미리보기 | 발표 없음 | 비공개 | 발표 없음 |
| 11월 18일 | Google | Gemini 4 Neon | Gemini API 유료 등급·Gemini for business, AI Pro·Ultra 구독자(Gemini 앱·Antigravity), Fairwind 참가 방어자 | $3 / $15 | 비공개 | Argon 판정을 이어받음(사이버·생물 위험 기준 도달 가능성 배제 못 함) |
| 11월 20일 | Thinking Machines | Inkling 2 Mini | Tinker·Tinker Playground, 허깅페이스, Ollama·vLLM 등 | $0.15 / $0.50(Tinker, 무료 등급 있음) | 공개(Apache 2.0) | 발표 없음 |

*발표일은 회사 소재지 기준이다. Hydrogen은 100만 토큰 문맥 전 구간에서 값이 같다. GPT-6.2 두 모델은 입력이 27만 2,000토큰을 넘는 요청에 입력 2배, 출력 1.5배 값을 받는다. Inkling 2 Mini의 Tinker 무료 등급은 문맥 6만 4,000토큰까지이고 이용 한도가 있다. 출처: [Carbon 일반 공개](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/), [Hydrogen 발표](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/), [Neon 발표](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/), [Gemini API 가격표](https://aistudio.google.com/docs/pricing), [GPT-6.2 발표](https://openai.com/index/introducing-gpt-6-2-astra-sol/)·[Astra API 문서](https://developers.openai.com/api/docs/models/gpt-6.2-astra)·[Sol API 문서](https://developers.openai.com/api/docs/models/gpt-6.2-sol)·[안전 문서](https://deploymentsafety.openai.com/gpt-6-2-astra-sol), [MAI Code 2 발표](https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/), [Inkling 2 Mini 발표](https://thinkingmachines.ai/news/inkling-2-mini/)·[허깅페이스](https://huggingface.co/thinkingmachines/Inkling-2-Mini)·[Tinker 가격표](https://tinker-docs.thinkingmachines.ai/tinker/models/models_and_pricing/), Google 안전·보안 보고서([Carbon](https://storage.googleapis.com/deepmind-media/gemini/gemini_4_carbon_safety_report.pdf)·[Hydrogen](https://storage.googleapis.com/deepmind-media/gemini/gemini_4_hydrogen_safety_report.pdf)·[Neon](https://storage.googleapis.com/deepmind-media/gemini/gemini_4_neon_safety_report.pdf)).*

## 11/10 — Gemini 4 Carbon 일반 공개

**[Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/)은 10일 Gemini 4 Carbon을 돈을 내는 개발자와 기업 모두에게 풀었다.** 10월 28일 공개 때는 사이버 방어 프로그램 Fairwind의 방어자에게만 먼저 준 모델이다([10월 30일 일일](/jogan/daily/2026-10-30/#tech)). 이제 Google AI Studio의 API와 Gemini for business로 쓸 수 있고, AI Ultra 구독자에게는 Antigravity와 Gemini 앱, 검색 AI 모드로 풀린다([11월 12일 일일](/jogan/daily/2026-11-12/#tech)).

앞 편이 날짜를 기다리던 도입가의 끝도 정해졌다. 100만 토큰당 입력 2달러·출력 10달러는 11월 30일까지이고, [가격표](https://aistudio.google.com/docs/pricing)에는 12월 1일부터 4달러·20달러로 오른다고 적혀 있다. API 무료 등급에서는 쓸 수 없다. 같은 공지에는 Carbon만의 안전·보안 보고서도 걸렸다.

## 11/12 — Gemini 4 Hydrogen

**[Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)은 12일 Gemini 4 Hydrogen을 개발자·기업·일반 이용자에게 전 세계로 내놨다.** 깊은 장기 추론을 맡는 Carbon·Argon과 달리 빠른 일상 코딩과 에이전트 작업을 맡는 모델이고, [모델 카드](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Hydrogen-Model-Card.pdf)에는 Carbon을 바탕으로 만들었다고 적혀 있다. 글·이미지·음성·동영상을 받아 글로 답하고, 문맥은 100만 토큰이며, 추론 강도에는 xhigh 단계가 새로 생겼다.

Gemini API·AI Studio와 Gemini for business, Gemini 앱에서 쓸 수 있고 구글 검색에서는 모든 이용자에게 풀린다. 무료 Gemini 앱 이용자에게는 질문에 맞을 때 자동으로 골라 쓰인다. 값은 100만 토큰당 입력 1.50달러·출력 7.50달러이고, 이 기간 Google 모델 가운데 API 무료 등급이 있는 것은 Hydrogen뿐이다([11월 13일 일일](/jogan/daily/2026-11-13/#tech)).

## 11/12 — Inkling 2 Small 가중치

**5일 출시 때 다음 주에 풀겠다고 한 Inkling 2 Small의 가중치가 12일 허깅페이스에 올라왔다.** [Thinking Machines](https://thinkingmachines.ai/news/inkling-2-small/)는 발표문 머리에 12일 날짜로 이 사실을 덧붙였고, [허깅페이스 저장소](https://huggingface.co/thinkingmachines/Inkling-2-Small)에 붙은 라이선스는 예고대로 Apache 2.0이다. 앞 편에서 다룬 Mistral Large 4·Kimi K3.1 Pro의 라이선스와 달리, 모델을 API로 다시 파는 사업에도 따로 계약을 요구하지 않는다.

## 11/17 — GPT-6.2 Astra·Sol

**[OpenAI](https://openai.com/index/introducing-gpt-6-2-astra-sol/)는 17일 GPT-6.2 Astra와 GPT-6.2 Sol을 ChatGPT Work와 Codex, API에 내놨다.** 회사는 Astra를 어려운 프로젝트용, Sol을 일상 업무용으로 들었고, [개발자 변경 기록](https://developers.openai.com/api/docs/changelog)에서는 Astra를 까다로운 추론·코딩에, Sol을 일상 코딩과 에이전트 작업에 쓰라고 안내했다. ChatGPT에서는 Plus·Pro·Enterprise·Edu 이용자가 쓸 수 있다([11월 18일 일일](/jogan/daily/2026-11-18/#tech)).

[API 문서](https://developers.openai.com/api/docs/models/gpt-6.2-astra)에 적힌 Astra 값은 100만 토큰당 입력 8달러·출력 40달러로 GPT-6 Astra(10달러·50달러, [9~10월 기획](/jogan/feature/ai-models-september-october/))보다 20% 낮고, [Sol](https://developers.openai.com/api/docs/models/gpt-6.2-sol)은 2달러·10달러로 GPT-6.1 Sol과 같다. 두 모델 모두 문맥은 105만 토큰이고 글과 이미지를 받는다.

## 11/17 — MAI Code 2·Code 2 Flash

**[Microsoft](https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/)는 17일 코딩 모델 MAI Code 2와 MAI Code 2 Flash를 GitHub Copilot에 내놨다.** 회사는 두 모델을 기업의 일상적인 코딩 작업용으로 만들었고, 기초 과학 연구나 아주 긴 에이전트 작업에는 아직 맞추지 않았다고 했다. Code 2는 여러 파일에 걸친 구현과 디버깅, 화면 코드를, Code 2 Flash는 코드 설명과 부분 수정처럼 양이 많은 일을 맡는다. Code 2 Flash는 Microsoft Foundry에서 제한적 미리보기로도 쓸 수 있고, 회사는 OpenRouter·Vercel 등에도 곧 올리겠다고 했다([11월 18일 일일](/jogan/daily/2026-11-18/#tech)).

발표문에는 100만 토큰당 값이 없고, 회사가 든 비용 비교는 판촉 기간의 50% 할인 값을 기준으로 했다. 가중치도 공개하지 않았다. 다만 같은 날 낸 [MAI Licensed Weights](https://microsoft.ai/news/introducing-mai-licensed-weights/)로 기업은 MAI 모델을 자기 Azure 환경에 들여 고쳐 쓸 수 있고, 회사가 든 고객 사례에는 Code 2와 Code 2 Flash를 고쳐 쓴 경우가 있다.

## 11/18 — Gemini 4 Neon

**[Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)은 18일 Gemini 4 Neon을 Gemini API 유료 등급과 Gemini for business에 내놨다.** 회사는 긴 작업용 Carbon과 빠른 일상 작업용 Hydrogen 사이에 이 모델을 두고, 복잡한 코딩과 분석적 추론, 기업 업무를 용도로 들었다. Gemini 앱과 Antigravity에서는 Google AI Pro·Ultra 구독자가 쓰고, Fairwind 프로그램의 사이버 방어자에게도 며칠에 걸쳐 열린다.

값은 100만 토큰당 입력 3달러·출력 15달러이고 캐시된 입력은 95% 싼 0.15달러다. 12월 1일부터 Carbon에 매겨질 4달러·20달러보다 25% 낮다. 문맥은 100만 토큰이고, API 무료 등급에서는 쓸 수 없다([11월 20일 일일](/jogan/daily/2026-11-20/#tech)).

## 11/20 — Inkling 2 Mini

**[Thinking Machines](https://thinkingmachines.ai/news/inkling-2-mini/)는 20일 Inkling 2 Mini를 내고 그 가중치를 [허깅페이스](https://huggingface.co/thinkingmachines/Inkling-2-Mini)에 Apache 2.0으로 공개했다.** 전체 매개변수 264억 개 가운데 토큰마다 34억 개를 쓰는 전문가 혼합(MoE) 모델이고, 가운데 층을 세 번씩 돌리므로 그만큼을 더해 세면 한 토큰에 54억 개를 쓴다. 글과 이미지를 받아 글로 답하며, 문맥은 최대 100만 토큰이다.

체크포인트 하나가 약 20GB여서, 회사는 메모리가 32GB 이상인 Apple 실리콘 기기 등에서 돌릴 수 있다고 안내했다. Ollama·vLLM·SGLang 같은 도구에서도 돌아가고, 회사 서비스 Tinker의 [가격표](https://tinker-docs.thinkingmachines.ai/tinker/models/models_and_pricing/)로는 100만 토큰당 입력 0.15달러·출력 0.50달러다. 문맥 6만 4,000토큰까지는 이용 한도 안에서 무료로 불러 쓰고 미세 조정할 수 있다([11월 22일 일일](/jogan/daily/2026-11-22/#tech)).

## 위험 판정과 제한 공개

**OpenAI는 GPT-6.2 두 모델을 사이버보안 위험의 위 단계로 다루고, Google은 세 모델에 서로 다른 판정을 냈다.** 회사마다 기준이 달라 판정을 서로 견줄 수는 없다. [OpenAI](https://deploymentsafety.openai.com/gpt-6-2-astra-sol)의 사이버보안 Critical은 방비가 단단한 실제 핵심 시스템 여럿에서 사람 손을 거치지 않고 아직 알려지지 않은 취약점을 찾아 공격 코드까지 만들거나, 큰 목표만 받고 새로운 공격 전략을 처음부터 끝까지 짜 실행할 수 있는 수준이다. Google의 임계 능력 수준(CCL)은 [보고서](https://storage.googleapis.com/deepmind-media/gemini/gemini_4_hydrogen_safety_report.pdf)의 정의로 대응책이 없으면 심각한 피해 위험이 커질 수 있는 능력 수준이다.

- **OpenAI:** [안전 문서](https://deploymentsafety.openai.com/gpt-6-2-astra-sol)는 Astra와 Sol 모두 자체 기준(Preparedness Framework)에서 사이버보안 Critical, 생물·화학 High에 이른다고 적었고, Astra는 AI 자기 개선(AI Self-improvement) 항목에서도 High에 이른다고 판단했다. 회사는 [발표](https://openai.com/index/introducing-gpt-6-2-astra-sol/)에서 사이버 안전장치를 더 조여 냈고, 그 때문에 정당한 취약점 연구 일부도 막힌다고 밝혔다. 검증된 방어자가 사이버 거절을 줄인 모델을 쓰는 OpenAI 프로그램 Daybreak에는 지금 GPT-6 Sol이 올라 있고, 회사는 GPT-6.2도 올리겠다고 했다.
- **Google:** [Hydrogen 보고서](https://storage.googleapis.com/deepmind-media/gemini/gemini_4_hydrogen_safety_report.pdf)는 Hydrogen이 화생방(CBRN)·사이버에서 자체 기준(Frontier Safety Framework)의 임계 능력 수준(CCL)에는 이르지 않았지만, 그에 앞서 경고하는 기준(alert threshold)에는 이르렀다고 적었다. 반면 [Neon](https://storage.googleapis.com/deepmind-media/gemini/gemini_4_neon_safety_report.pdf)과 [Carbon](https://storage.googleapis.com/deepmind-media/gemini/gemini_4_carbon_safety_report.pdf) 보고서는 두 모델의 능력이 Argon보다 크게 늘지 않았다며, 모델 바깥의 안전장치를 걷어 낸 상태라면 모델이 사이버와 생물 정보 위험에서 CCL에 이르렀을 가능성을 배제할 수 없다는 Argon의 판정을 이어 썼다. Carbon 보고서는 취약점 공격 평가 점수가 오른 것을 보고 사이버 오용 방어를 Argon 때보다 굳혔다고 덧붙였다.
- **Microsoft:** [MAI Code 2 발표](https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/)에는 위험 판정이 없다.
- **Thinking Machines:** [Inkling 2 Mini 발표](https://thinkingmachines.ai/news/inkling-2-mini/)에는 위험 등급이 없다. 대신 회사는 층 반복 횟수를 바꿀 수 있는 연구용 변형에서 반복을 늘려도 에이전트의 방해 행동을 재는 시험 점수가 오르지 않았고, 이 크기에서는 모델의 추론 과정을 감시하기가 뚜렷이 어려워지지 않았다고 밝혔다.

**해설:** 판정이 높다고 공개 범위가 좁아진 것은 아니다. OpenAI는 사이버보안 Critical로 다루는 두 모델을 출시 당일 API에 풀었고, Carbon도 공개 13일 만에 유료 개발자 모두에게 열렸다. 두 회사가 밝힌 대응은 위험한 요청을 거절하고 막는 안전장치를 조이는 것이었다.

## 외부 평가

**Hydrogen은 추론 강도를 low에서 xhigh로 올리자 Artificial Analysis 점수가 27에서 54로 두 배가 됐다.** 아래는 회사가 아닌 Artificial Analysis, Vals, ARC Prize가 직접 잰 결과이고, 모델마다 가장 높은 점수와 그때의 설정을 적었다. 세 기관이 아직 결과를 내지 않은 MAI Code 2·Code 2 Flash는 표에 없다.

| 모델 | Artificial Analysis 지능 지수(5.0.2 버전) | Vals 지수(2.2 버전) | ARC-AGI-2 |
|---|---|---|---|
| Gemini 4 Hydrogen | 54(xhigh) | 67.07% ±1.06(xhigh) | 92.5%(xhigh) |
| GPT-6.2 Astra | 62(max) | 66.27% ±1.00(max) | 95.8%(max) |
| GPT-6.2 Sol | 57(max) | 65.07% ±0.98(max) | 85.8%(max) |
| Gemini 4 Neon | 62(xhigh) | 69.23% ±1.00(xhigh) | 93.8%(medium) |
| Inkling 2 Mini | 20(설정 표기 없음) | 44.03% ±1.15(추론 강도 0.99) | 49.3%(xhigh) |

*ARC Prize는 Neon을 high로 잴 때 API 문제로 비공개 시험 과제 8개를, medium으로 잴 때 1개를 끝내지 못했고, xhigh는 API 응답이 오래 걸려 시험을 마치지 못했다고 밝혔다. 그래서 Neon 칸만 medium 점수다.*

- **Artificial Analysis 지능 지수:** 평가 아홉 개를 지식 업무·코딩·과학·일반에 25%씩 나눠 묶은 점수다. 11월 들어 터미널 작업 평가를 Terminal-Bench 4.1로 바꾸고 코딩 평가(FrontierCode)의 채점을 고쳐 모든 모델을 다시 매긴 5.0.2 버전 점수이고, 11월 26일 각 모델 페이지에서 조회했다([Hydrogen](https://artificialanalysis.ai/models/gemini-4-hydrogen), [Astra](https://artificialanalysis.ai/models/gpt-6-2-astra), [Sol](https://artificialanalysis.ai/models/gpt-6-2-sol), [Neon](https://artificialanalysis.ai/models/gemini-4-neon), [Inkling 2 Mini](https://artificialanalysis.ai/models/inkling-2-mini), [버전 기록](https://artificialanalysis.ai/methodology/intelligence-benchmarking)).
- **Vals 지수:** 금융·코딩·법률·세무 업무에서 AI가 여러 단계를 해내는 능력을 재는 지수다. 11월 21일 갱신된 [지수 페이지](https://www.vals.ai/benchmarks/vals_index)와 각 모델 페이지에서 11월 26일 조회한 점수이고, ±는 표준오차다([Hydrogen](https://www.vals.ai/models/google_gemini-4-hydrogen), [Astra](https://www.vals.ai/models/openai_gpt-6.2-astra), [Sol](https://www.vals.ai/models/openai_gpt-6.2-sol), [Neon](https://www.vals.ai/models/google_gemini-4-neon), [Inkling 2 Mini](https://www.vals.ai/models/thinkingmachines_inkling-2-mini)).
- **ARC-AGI-2:** 처음 보는 퍼즐의 규칙을 찾아내는 시험으로, ARC Prize가 비공개 시험 세트(Semi-Private)로 검증한 최고점이다. 결과는 Hydrogen이 12일, Astra·Sol이 17일, Neon이 18일, Inkling 2 Mini가 20일 나왔다([Hydrogen](https://arcprize.org/results/google-gemini-4-hydrogen), [Astra](https://arcprize.org/results/openai-gpt-6-2-astra), [Sol](https://arcprize.org/results/openai-gpt-6-2-sol), [Neon](https://arcprize.org/results/google-gemini-4-neon), [Inkling 2 Mini](https://arcprize.org/results/thinky-inkling-2-mini)).

설정을 올리면 점수와 함께 비용도 오른다. [Artificial Analysis](https://x.com/ArtificialAnlys/status/2120941516407337325)에서 Hydrogen의 xhigh는 high보다 출력 토큰을 두 배 가까이 쓰고 3점 높았으며, 과제당 비용은 high 1.87달러, xhigh 3.16달러였다. 평가 버전도 점수를 바꿔서, 18일 Neon 출시 때 [Artificial Analysis](https://x.com/ArtificialAnlys/status/2123170645777526962)가 낸 xhigh 점수는 61이었고 5.0.2 버전 페이지에서는 62다.

Vals 지수 시험을 한 번 치르는 데 든 값은 GPT-6.2 Sol 3.18달러, Inkling 2 Mini 3.20달러, Neon 7.41달러, Hydrogen 7.75달러, Astra 10.68달러였다. 토큰당 값은 Hydrogen이 Neon의 절반인데도 시험 한 번의 값은 더 들었다.

## 다음에 볼 것

- **Carbon 값이 12월 1일 예고대로 오르는지.**
  [Gemini API 가격표](https://aistudio.google.com/docs/pricing)는 Carbon의 100만 토큰당 입력 2달러·출력 10달러가 11월 30일까지이고 12월 1일부터 4달러·20달러가 된다고 적었다.
  12월 1일 이후 같은 가격표의 Carbon 줄이 4달러·20달러로 바뀌었는지, 도입가 기간이 늘었다는 공지가 붙었는지 보면 된다.
  바뀌면 3달러·15달러인 Neon이 Carbon보다 25% 싼 모델이 되고, 도입가가 이어지면 Carbon이 Neon보다 싼 값에 남는다.
- **GPT-6.2가 방어자용 Daybreak에 오르는지.**
  [OpenAI](https://openai.com/index/introducing-gpt-6-2-astra-sol/)는 GPT-6.2를 사이버 안전장치를 조여 냈고, 사이버 거절을 줄인 모델을 주는 Daybreak에는 지금 GPT-6 Sol이 올라 있다며 GPT-6.2도 올리겠다고 했다. 날짜는 밝히지 않았다.
  [Daybreak 안내](https://openai.com/daybreak/)와 OpenAI 발표에 GPT-6.2 모델이 이름을 올리는지 보면 된다.
  오르면 검증된 방어자는 사이버보안 Critical로 다뤄지는 모델을 거절이 적은 형태로 쓰게 되고, 오르지 않으면 방어자는 Daybreak에서 GPT-6 Sol을 계속 쓰게 된다.
