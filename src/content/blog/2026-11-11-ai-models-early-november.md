---
title: "AI 모델 출시 — 10월 28일~11월 9일"
description: "10월 28일부터 11월 9일까지 Google, Mistral, Thinking Machines, Anthropic이 새 AI 모델을 냈다. Gemini 4 Carbon, Mistral Large 4, Inkling 2 Small, Claude Fable 5.2를 발표일·쓸 수 있는 곳·값·가중치 공개 여부로 나란히 놓고, 가중치 라이선스와 일부에게만 먼저 준 모델, 외부 기관의 평가를 측정 조건과 함께 정리했다."
pubDate: 2026-11-11
tags: ["기획", "테크"]
period: { from: 2026-10-28, to: 2026-11-09 }
highlights:
  - { label: "다룬 모델", value: "4개", note: "네 회사, 10/28~11/9 발표" }
  - { label: "100만 토큰당 출력 값", value: "$1~$40", note: "Tinker·각 회사 API" }
  - { label: "가중치 공개", value: "2개", note: "Mistral·Kimi, Inkling은 예정" }
---

## 먼저 요점만

1. **10월 28일부터 11월 9일 사이 네 회사가 새 모델을 냈다.** Gemini 4 Carbon, Mistral Large 4, Inkling 2 Small, Claude Fable 5.2이고, 100만 토큰당 출력 값은 Inkling 2 Small의 1달러부터 Fable 5.2의 40달러까지다. 이 가운데 Carbon은 아직 일부 사이버 방어자만 쓸 수 있다.
2. **매개변수가 1조 개 이상인 모델 둘의 가중치가 풀렸다.** Mistral Large 4와 Kimi K3.1 Pro로, 둘 다 상업적으로 쓸 수 있지만, 모델을 API로 파는 사업자에게는 따로 계약을 요구한다(문샷AI는 매출 2,000만 달러가 넘는 곳에만). Inkling 2 Small은 Apache 2.0으로 풀겠다고 했고 10일까지는 올라오지 않았다.
3. **사이버 능력이 큰 모델은 검증을 거친 곳에 먼저, 또는 따로 줬다.** Google은 Carbon을 일부 방어자에게 먼저 풀었고, Anthropic은 안전장치를 뺀 Mythos 5.2를 검증 기관에만 준다. Mistral도 사이버 작업에 맞춘 변형을 계약을 맺은 파트너에게만 미리 보여 준다.

10월 14~28일에 나온 모델은 [AI 모델 출시 — 10월 14~28일](/jogan/feature/ai-models-late-october/)에 정리했다. 이 글은 그 뒤 조간 일일 글에 실린 범용 모델 넷을 같은 항목으로 다룬다. 10월 28일 공개된 Carbon은 앞 편이 나온 뒤 [10월 30일 일일](/jogan/daily/2026-10-30/#tech)에 실려 여기서 다루고, 동영상 모델 Gemini Omni 1.2 Flash([11월 6일 일일](/jogan/daily/2026-11-06/#tech))처럼 영상·음성 전용 모델은 뺐다.

## 한눈에 보는 네 모델

**네 모델은 누가 쓸 수 있는지부터 갈린다.** Carbon과 Mythos 5.2는 정해진 기관에만 열려 있고, 나머지는 서비스나 API로 누구나 쓸 수 있다. 값은 앱 구독료가 아니라 다른 프로그램에서 모델을 불러 쓰는 API의 사용료이고, 같은 입력을 반복해 보내면 더 낮은 캐시 값을 받으므로 표에는 캐시되지 않은 입력 값을 적었다. 위험 판정 칸에는 회사가 자체 기준으로 내놓은 것만 적었다.

| 발표(현지) | 회사 | 모델 | 쓸 수 있는 곳 | 100만 토큰당 값(캐시 안 된 입력/출력) | 가중치 | 회사가 밝힌 위험 판정 |
|---|---|---|---|---|---|---|
| 10월 28일 | Google | Gemini 4 Carbon | 일부 사이버 방어자(Fairwind 프로그램), 일반 공개 날짜 미정 | $2 / $10(도입가, 끝나면 $4 / $20) | 비공개 | Carbon만의 판정은 내지 않음 |
| 10월 29일 | Mistral | Mistral Large 4(가중치 공개 버전) | Mistral Studio·API, OpenRouter, Microsoft Foundry, 허깅페이스 | $0.70 / $2.10 | 공개(Mistral 자체 라이선스) | 발표 없음 |
| 11월 5일 | Thinking Machines | Inkling 2 Small | Tinker·Tinker Playground | $0.30 / $1.00 | 공개 예정(Apache 2.0) | 발표 없음 |
| 11월 9일 | Anthropic | Claude Fable 5.2 / Claude Mythos 5.2 | Fable: Claude 유료 요금제·Claude Code, API, Amazon Bedrock·Google Cloud·Microsoft Foundry / Mythos: 검증 프로그램을 거친 기관 | $8 / $40(빠른 모드 $16 / $80) | 비공개 | 생물·화학 CB-1 보호 적용, 사이버는 자체 기준의 낮은 범주 |

*발표일은 회사 소재지 기준이다. Carbon의 도입가가 언제 끝나는지는 발표되지 않았다. Mythos 5.2의 값과 사양은 Fable 5.2와 같다. Inkling 2 Small의 값은 Tinker에서 모델을 불러 쓰는 값이고, 미세 조정 학습은 100만 토큰당 1.50달러(문맥 6만 4,000토큰 기준)다. 출처: [Gemini 4 Carbon 발표](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/), [Mistral Large 4 발표](https://mistral.ai/news/mistral-large-4-oss/)·[공개 시각](https://x.com/MistralAI/status/2115811242556137820), [Inkling 2 Small 발표](https://thinkingmachines.ai/news/inkling-2-small/)·[Tinker 가격표](https://tinker-docs.thinkingmachines.ai/tinker/models/models_and_pricing/), [Fable 5.2·Mythos 5.2 발표](https://www.anthropic.com/claude-fable-and-mythos-5-2)·[API 문서](https://platform.claude.com/docs/en/models/fable-5-2/overview)·[요금제 안내](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan)·[시스템 카드](https://www.anthropic.com/document/claude-fable-5-2-mythos-5-2-system-card).*

## 10/28 — Gemini 4 Carbon

**[Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/)은 28일 Gemini 4 Carbon을 공개하고, 그 주부터 일부 사이버 방어자에게 먼저 준다고 밝혔다.** 오래 걸리는 엔지니어링 문제와 에이전트 작업, 그리고 취약점을 찾아 검증하고 고치는 사이버 방어를 용도로 내세운 모델이다. 회사는 내부 시험에서 Carbon이 Gemini 4 Argon보다 안전한 코드를 짜는 성공률이 두 배 넘게 높았다고 밝혔다.

이어 사이버 방어 프로그램 [Fairwind](https://deepmind.google/fairwind-program/)로 신뢰할 수 있는 파트너를 차례로 늘리고, 개발자·기업·일반 이용자에게는 의견을 받아 안전장치를 다듬은 뒤 내놓겠다고 했지만 날짜는 밝히지 않았다. 값은 Argon의 도입가와 같은 100만 토큰당 입력 2달러·출력 10달러로 시작해 도입 기간이 끝나면 4달러·20달러가 되고, 캐시된 입력은 95% 싸다.

## 10/29 — Mistral Large 4

**[Mistral](https://mistral.ai/news/mistral-large-4-oss/)은 29일 Mistral Large 4를 고친 버전을 내고 그 가중치를 공개했다.** 6일 공개 미리보기로 낸 멀티모달 모델([10월 8일 일일](/jogan/daily/2026-10-08/#tech))을 손본 것으로, 전체 매개변수(학습으로 정해지는 모델 내부의 값) 1조 개 가운데 한 번에 520억 개를 쓰는 전문가 혼합(MoE) 구조로, 요청마다 일부만 골라 계산한다. 회사는 미리보기 때보다 터미널 작업 평가(Terminal-Bench 4.0) 점수가 13%포인트 올랐고 출력 토큰은 30% 줄었다고 밝혔다.

Mistral Studio와 API, OpenRouter, 엔비디아 호스팅, Microsoft Foundry에서 쓸 수 있고, 가중치는 [허깅페이스](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B)에서 내려받는다. API 값은 100만 토큰당 입력 0.70달러·출력 2.10달러로, 미리보기 때의 1.36달러·4.18달러([AI 모델 3주](/jogan/feature/ai-models-three-weeks/))에서 절반 가까이 내렸다.

## 11/5 — Inkling 2 Small

**[Thinking Machines](https://thinkingmachines.ai/news/inkling-2-small/)는 5일 Inkling 2 Small을 자사 서비스 Tinker에서 가중치를 공개하지 않은 채 먼저 내놨다.** 전체 매개변수 5,940억 개 가운데 한 번에 170억 개를 쓰는 전문가 혼합 구조이고, 글과 이미지를 받지만 음성은 받지 않는다. 회사는 에이전트 코딩, 이미지 이해, 지식 업무, 이용자의 미세 조정을 용도로 들었다.

Tinker는 모델을 불러 쓰거나 자기 데이터로 미세 조정하는 서비스이고, [가격표](https://tinker-docs.thinkingmachines.ai/tinker/models/models_and_pricing/)로 100만 토큰당 입력 0.30달러·출력 1달러다. 회사는 자체·외부 안전성 시험과 레드팀 평가를 마치는 대로 다음 주 Apache 2.0 라이선스로 전체 가중치를 풀고, 몇 주 안에 다른 플랫폼에도 내놓겠다고 했다([11월 8일 일일](/jogan/daily/2026-11-08/#tech)).

## 11/9 — Claude Fable 5.2·Mythos 5.2

**[Anthropic](https://www.anthropic.com/claude-fable-and-mythos-5-2)은 9일 Claude Fable 5.2와, 같은 기반 모델에서 사이버·생물학 안전장치 일부를 뺀 Claude Mythos 5.2를 공개했다.** Fable 5.2는 침투 테스트·익스플로잇 생성 같은 고위험 사이버 작업과 연구용 생물학 작업 대부분을 분류기로 막고, API에서 폴백을 켜 두면 막힌 요청을 다른 Claude 모델에 다시 보내지만, 폴백 모델이 정해지지 않은 분류의 요청은 그대로 거절된다. 회사는 몇 시간씩 이어지는 에이전트 작업과 여러 단계의 조사를 용도로 들었고, 5.1보다 출력이 최대 30% 빠르다고 밝혔다.

[API 문서](https://platform.claude.com/docs/en/models/fable-5-2/overview)에 적힌 값은 100만 토큰당 입력 8달러·출력 40달러여서 Fable 5.1(10달러·50달러, [9~10월 기획](/jogan/feature/ai-models-september-october/))보다 20% 낮다. 무료 요금제를 뺀 Claude [유료 요금제](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan)와 API, Amazon Bedrock·Google Cloud·Microsoft Foundry에서 쓸 수 있다([11월 10일 일일](/jogan/daily/2026-11-10/#tech)). Max 요금제 등에는 기본으로 들어 있고, Pro와 Team 표준 좌석에서는 쓰는 만큼 내는 사용량 크레딧으로 쓴다.

## 가중치와 라이선스

**10월 29일과 11월 5일, 매개변수가 1조 개 이상인 모델 둘의 가중치가 풀렸다.** Mistral Large 4에 이어 [문샷AI](https://x.com/Kimi_Moonshot/status/2118010528123773297)가 베이징 시간 5일 0시(협정 세계시 4일 16시)에 Kimi K3.1 Pro의 가중치를 [허깅페이스](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)에 올렸다. 전체 2조 8,000억 개 가운데 1,040억 개를 쓰는 모델로, 문샷AI는 앞 편이 다룬 10월 24일 출시 때 11월 4일까지 풀겠다고 했다.

다만 두 회사 모두 가중치를 받아 모델을 API로 파는 사업에는 따로 계약을 요구한다.

- **Mistral Large 4:** [Mistral 생태계 공개 가중치 라이선스](https://mistral.ai/news/mistral-large-4-oss/)는 MIT 라이선스를 고친 것으로 누구나 쓰고 고치고 상업적으로 쓸 수 있지만, 모델을 서비스로 파는(Model-as-a-Service) 사업자는 Mistral과 따로 상업 라이선스를 맺어야 한다.
- **Kimi K3.1 Pro:** [자체 라이선스](https://huggingface.co/moonshotai/Kimi-K3.1-Pro/blob/main/LICENSE)도 사용·수정·판매를 허용하는데, 모델을 서비스로 파는 사업을 하면서 이용자와 계열사의 매출을 합쳐 연속 12개월에 2,000만 달러를 넘으면 문샷AI와 따로 계약해야 한다. 월 이용자 1억 명 또는 월매출 2,000만 달러를 넘는 상품에는 화면에 "Kimi K3.1-Pro"를 표시해야 하고, 내부에서만 쓰는 경우는 두 조건에서 빠진다.
- **Inkling 2 Small:** [Thinking Machines](https://thinkingmachines.ai/news/inkling-2-small/)가 예고한 Apache 2.0은 이런 사업 조건 없이 상업적 사용과 재배포를 허용한다. 가중치는 10일까지 [허깅페이스](https://huggingface.co/thinkingmachines) Thinking Machines 저장소에 올라오지 않았다.

**해설:** 같은 '공개 가중치'라도 라이선스가 쓸 수 있는 범위를 정한다. 자기 서비스 안에 모델을 넣어 쓰는 회사와 모델 자체를 API로 다시 파는 회사는 같은 가중치를 받아도 지켜야 할 조건이 다르다.

## 위험 판정과 제한 공개

**사이버 능력을 앞세운 모델을 검증된 곳에 먼저, 또는 따로 준 회사가 셋이다.** 회사마다 기준이 달라 판정을 서로 견줄 수는 없다.

- **Google:** [Carbon 발표](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/)는 Carbon이 Argon과 같은 여러 겹의 안전·보안 장치 위에 만들어졌다며 [Argon의 안전·보안 보고서](https://storage.googleapis.com/deepmind-media/gemini/gemini_4_safety_report.pdf)를 걸었고, Carbon만의 위험 판정은 따로 내지 않았다. 그 보고서는 Argon이 사이버와 생물학에서 자체 기준(Frontier Safety Framework)의 위험 수준에 이르렀을 가능성을 배제할 수 없어 안전장치를 썼다고 적었다. 회사는 미국 정부의 자발적인 출시 전 모델 시험에도 참여하고 있다고 밝혔다.
- **Anthropic:** [시스템 카드](https://www.anthropic.com/document/claude-fable-5-2-mythos-5-2-system-card)는 Mythos 5.2가 생물·화학에서 자체 기준의 높은 단계(CB-2)는 넘지 않아 낮은 단계(CB-1) 보호 조치를 적용하고, 사이버는 자체 기준(Frontier Compliance Framework)의 낮은 능력 범주에 든다고 판단했다. 안전장치를 뺀 Mythos 5.2는 사이버보안·생명과학 검증 프로그램을 거친 기관에만 준다.
- **Mistral:** [Mistral](https://mistral.ai/news/mistral-large-4-oss/)은 정해진 위험 등급을 내지 않았지만, 실제 공격에 도움을 줄 가능성을 보고 안전장치를 고치고 있다고 밝혔다. 사이버 작업에 맞춘 변형은 엄격한 심사와 계약상 안전장치를 거친 설계 파트너에게만 미리 열었다.

반면 [Thinking Machines](https://thinkingmachines.ai/news/inkling-2-small/)는 등급 대신 가중치 공개를 자체·파트너의 안전성 평가가 끝난 뒤로 미뤘다.

**해설:** 판정이 없거나 낮다는 것이 더 안전하다는 뜻은 아니다. Google은 새 모델의 판정을 따로 내지 않았고 Anthropic의 판정도 자기 체계 안의 위치여서, 독자가 볼 수 있는 공통된 신호는 누구에게 먼저 풀었는지다.

## 외부 평가

**같은 지수 안에서도 버전과 추론 설정이 바뀌면 점수가 달라진다.** 아래는 회사가 아닌 Artificial Analysis, Vals, ARC Prize가 직접 잰 결과다. Artificial Analysis 점수는 Carbon·Mistral을 5.0, Inkling·Fable 5.2를 5.0.1로 잰 것이어서 칸끼리 바로 견줄 수 없다.

| 모델 | Artificial Analysis 지능 지수(평가 버전) | Vals 지수(2.2 버전) | ARC-AGI-2 |
|---|---|---|---|
| Gemini 4 Carbon | 59(5.0, high), 5.0.1에서 60 | 70.45% ±0.97(high) | — |
| Mistral Large 4 | 26(5.0, high) | 56.53% ±1.26(high) | — |
| Inkling 2 Small | 31(5.0.1, 설정 표기 없음) | 56.08% ±1.18 | 81.7%(xhigh) |
| Claude Fable 5.2 | 65(5.0.1, max, 기본 폴백 켬) | 71.31% ±0.96(high, 1.88% 과제를 폴백 모델이 풂) | 93.8%(xhigh) |

- **Artificial Analysis 지능 지수:** 평가 아홉 개를 지식 업무·코딩·과학·일반에 25%씩 나눠 묶은 점수다. 10월 27일 나온 5 버전으로 Carbon(28일)과 Mistral(29일)을 쟀고, 11월 들어 물리학 문제 평가(CritPt v2)의 채점을 고쳐 모든 모델을 다시 채점한 5.0.1 버전에서 Inkling(5일)과 Fable 5.2(9일)를 쟀다([Carbon](https://x.com/ArtificialAnlys/status/2115494553780367384), [Mistral](https://x.com/ArtificialAnlys/status/2115820547103952925), [Inkling](https://x.com/ArtificialAnlys/status/2118493376186388530), [Fable 5.2](https://x.com/ArtificialAnlys/status/2119878995386982508), [버전 기록](https://artificialanalysis.ai/methodology/intelligence-benchmarking)).
- **Vals 지수:** 금융·코딩·법률·세무 업무에서 AI가 여러 단계를 해내는 능력을 재는 지수다. 각 모델 페이지에서 11월 10일 조회한 점수이고, Inkling은 회사가 권한 설정(추론 강도 0.99)으로 쟀으며 ±는 표준오차다([Carbon](https://www.vals.ai/models/google_gemini-4-carbon), [Mistral](https://www.vals.ai/models/mistralai_mistral-large-4-oss), [Inkling](https://www.vals.ai/models/thinkingmachines_inkling-2-small), [Fable 5.2](https://web.archive.org/web/20261110084510/https://www.vals.ai/models/anthropic_claude-fable-5-2)).
- **ARC-AGI-2:** 처음 보는 퍼즐의 규칙을 찾아내는 시험으로, ARC Prize가 비공개 시험 세트(Semi-Private)로 검증한 최고점이다. 결과는 Inkling이 6일, Fable 5.2가 9일 나왔다([Inkling](https://arcprize.org/results/thinky-inkling-2-small), [Fable 5.2](https://arcprize.org/results/anthropic-claude-fable-5-2)).

폴백은 Anthropic 모델에서 안전 분류기가 거절한 요청을 [다른 Claude 모델이 대신 푸는](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback) 기능이다. Artificial Analysis는 Fable 5.2를 이 기능을 켠 채 쟀고, Vals에서는 Fable 5.2가 거절한 과제 26개(1.88%)를 다른 모델이 풀었으므로, 두 점수에는 다른 모델의 몫이 조금 섞여 있다.

같은 모델 안에서도 설정에 따라 점수가 갈린다. [Artificial Analysis](https://x.com/ArtificialAnlys/status/2119878995386982508)에서 Fable 5.2는 max에서 65, high에서 62였고, [ARC Prize](https://arcprize.org/results/anthropic-claude-fable-5-2)에서는 오히려 xhigh(93.8%)가 max(92.5%)보다 높았다. 또 Carbon의 59와 60은 같은 모델을 5 버전과 5.0.1 버전으로 잰 값이어서, [앞 편](/jogan/feature/ai-models-late-october/)에 실은 4.3 버전 점수와는 바로 견줄 수 없다.

Vals 지수 시험을 한 번 치르는 데 든 값도 모델마다 달라서, Inkling 2 Small 3.51달러, Mistral Large 4 3.72달러, Carbon 10.51달러(정가 기준), Fable 5.2 17.94달러였다.

## 다음에 볼 것

- **Inkling 2 Small 가중치가 예고대로 풀리는지.**
  [Thinking Machines](https://thinkingmachines.ai/news/inkling-2-small/)는 5일 발표에서 안전성 평가를 마친 뒤 다음 주 Apache 2.0으로 전체 가중치를 풀겠다고 했고, 가중치는 10일까지 [허깅페이스](https://huggingface.co/thinkingmachines) 저장소에 없다.
  이번 주 안에 이 저장소에 Inkling 2 Small이 올라오는지, 붙은 라이선스가 Apache 2.0인지 보면 된다.
  올라오면 이 기간 가중치를 내려받을 수 있는 모델이 셋이 되고, 그중 사업 조건이 없는 라이선스는 이것 하나다. 올라오지 않으면 공개 시점은 회사가 안전성 평가 결과와 함께 내놓을 다음 공지에 달린다.
- **Carbon이 개발자에게 열리는 날과 도입가가 끝나는 날.**
  [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/)은 Carbon을 일부 사이버 방어자에게 먼저 주고 개발자·기업·일반 이용자에게는 곧 내놓겠다고 했지만 날짜를 밝히지 않았고, 도입가가 언제 끝나는지도 정하지 않았다.
  Gemini API의 [모델 목록](https://ai.google.dev/gemini-api/docs/models)과 [가격표](https://ai.google.dev/gemini-api/docs/pricing)에 Carbon이 오르는지, 오른다면 4달러·20달러로 바뀌는 날이 적혀 있는지 보면 된다.
  오르면 이 기간 모델 가운데 정해진 기관에만 주는 것은 Mythos 5.2 하나가 되고, Carbon도 누구나 API로 불러 쓸 수 있게 된다. 오르지 않으면 Carbon은 외부 평가 점수만 먼저 나왔을 뿐 일부 방어자에게만 열린 모델로 남는다.
