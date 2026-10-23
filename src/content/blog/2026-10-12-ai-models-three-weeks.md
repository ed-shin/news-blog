---
title: "AI 모델 출시·가격·가중치 공개 — 9월 20일~10월 12일"
description: "9월 20일부터 10월 12일까지 일곱 회사가 새 AI 모델 열세 개를 내놨다. 같은 급 모델의 값은 절반 가까이 내렸고, 1조·5,010억 매개변수 모델은 가중치 공개를 예고했다. 새 모델 일부는 사이버 방어 쪽에 먼저 풀렸다."
pubDate: 2026-10-12
updatedDate: 2026-10-23
corrections:
  - date: 2026-10-23
    text: "제목을 「AI 모델 3주 — 새 모델 열세 개, 절반이 된 값, 공개를 앞둔 가중치」에서 「AI 모델 출시·가격·가중치 공개 — 9월 20일~10월 12일」로 바꾸고, 소제목을 다루는 대상으로 고쳤다. 본문은 문장을 이어 쓰고 출처를 문장 끝 괄호 대신 매체·기관·회사 이름에 걸었다. 사실과 숫자는 바꾸지 않았다."
tags: ["기획", "테크"]
searchTitle: "AI 모델 출시 정리 — 2026년 9~10월 새 모델·가격·오픈웨이트 | 견문록"
period: { from: 2026-09-20, to: 2026-10-12 }
highlights:
  - { label: "새로 나온 모델", value: "13개", note: "일곱 회사, 9/20~10/7 발표" }
  - { label: "GPT-6 Sol 출력 값", value: "$20 → $10", note: "100만 토큰당, 직전 모델 대비" }
  - { label: "가중치 공개 예고", value: "2개", note: "1조·5,010억 매개변수, 10월 하순" }
---

## 먼저 요점만

1. **3주 사이 일곱 회사가 새 AI 모델 열세 개를 내놨고, 같은 급의 값은 절반 가까이 내렸다.** OpenAI의 GPT-6 Sol은 직전 모델보다 출력 값이 절반이 됐다.
2. **큰 모델의 가중치를 내려받게 하겠다는 회사가 둘 나왔다.** Mistral Large 4와 Reflection AI의 Beam으로, 둘 다 10월 하순 공개를 예고했고 아직 풀리지는 않았다.
3. **새 모델 일부는 보안 쪽으로 먼저 갔다.** 구글은 Gemini 4 Argon을 사이버 방어자에게 먼저 풀었고, OpenAI와 Anthropic도 새 모델의 보안 쪽 능력을 일반 공개와 따로 다뤘다.

## 한눈에 보는 3주

표에는 이 기간 조간 일일 글에 실린 새 모델을 모았고, 값은 100만 토큰당 입력·출력 가격이다. 회사들이 내놓은 성능 수치는 대부분 자체 평가라 표에 넣지 않았다.

| 발표 | 회사 | 모델 | 값(입력 / 출력) | 기록 |
|---|---|---|---|---|
| 9/20 | 알리바바 | Qwen-Image-2.1(이미지) | 가중치 공개, 연구용 라이선스 | [9월 21일 일일](/jogan/daily/2026-09-21/#tech) |
| 9/21 | xAI | Grok 4.7 | $2 / $6 | [9월 22일 일일](/jogan/daily/2026-09-22/#tech) |
| 9/22 | Anthropic | Claude Opus 5.5 | $4 / $20 | [9월 23일 일일](/jogan/daily/2026-09-23/#tech) |
| 9/22 | OpenAI | GPT-6 Sol · GPT-6 Luna | $2 / $10 · $0.10 / $0.50 | [9월 24일 일일](/jogan/daily/2026-09-24/#tech) |
| 9/23 | 구글 | Gemini 3.8 Flash TTS · Flash-Lite TTS(음성) | — | [9월 24일 일일](/jogan/daily/2026-09-24/#tech) |
| 9/28 | Anthropic | Claude Sonnet 5.5 | $2 / $10 | [9월 30일 일일](/jogan/daily/2026-09-30/#tech) |
| 9/29 | OpenAI | GPT-6.1 Sol | $2 / $10 | [9월 30일 일일](/jogan/daily/2026-09-30/#tech) |
| 9/30 | 구글 | Gemini 4 Argon | 도입가 $2 / $10, 이후 $4 / $20 | [10월 2일 일일](/jogan/daily/2026-10-02/#tech) |
| 10/5 | Reflection AI | Beam | 대기 명단, 가중치 10월 하순 공개 예정 | [10월 7일 일일](/jogan/daily/2026-10-07/#tech) |
| 10/6 | Mistral | Mistral Large 4 | $1.36 / $4.18 | [10월 8일 일일](/jogan/daily/2026-10-08/#tech) |
| 10/7 | Anthropic | Claude Haiku 5.5 | $0.10 / $0.50(입력 10만 토큰 이하) | [10월 8일 일일](/jogan/daily/2026-10-08/#tech) |

## 모델 가격

**OpenAI는 GPT-6 Sol의 값을 직전 모델의 절반으로 매겼다.** [벤처비트](https://venturebeat.com/technology/openai-releases-gpt-6-sol-and-luna-models-slashing-api-costs-50-or-more)에 따르면 GPT-6 Sol은 100만 토큰당 입력 2달러·출력 10달러로 직전 GPT-5.6 Sol의 4달러·20달러에서 절반이 됐고, 작은 모델 GPT-6 Luna의 출력 값도 1.20달러에서 0.50달러로 내렸다. OpenAI 대변인은 이 매체에 한시 할인이 아니라 영구 가격이라고 확인했다.

다른 회사도 값을 내리거나 그대로 뒀다. [Anthropic](https://www.anthropic.com/claude-opus-5-5)은 Claude Opus 5.5의 토큰 값을 직전 Opus 5보다 20% 낮췄다고 밝혔고, [Claude Haiku 5.5](https://www.anthropic.com/claude-haiku-5-5)는 Haiku 4.5보다 평균 약 75% 싸다고 밝혔다. [xAI](https://x.ai/news/grok-4-7)는 Grok 4.7을 직전 모델과 같은 값에 내놨고, [Claude Sonnet 5.5](https://www.anthropic.com/claude-sonnet-5-5)도 값을 그대로 뒀다.

같은 값에 더 높은 급의 성능을 내세운 경우도 있다. [The Next Web](https://thenextweb.com/news/openai-gpt-6-1-sol-price-astra-devday)에 따르면 OpenAI는 GPT-6.1 Sol이 상위 모델 GPT-6 Astra에 가까운 성능을 Astra 값의 5분의 1에 낸다고 주장했다.

**해설:** 토큰 값은 AI를 쓰는 쪽의 비용이라, 값이 내리면 오래 생각하거나 여러 단계를 도는 작업처럼 토큰을 많이 쓰는 일을 맡기기 쉬워진다. 다만 그만큼 비용이 새는 자리도 생긴다. 개발자 [사이먼 윌리슨](https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/)은 코딩 에이전트가 돈이 드는 코드를 쉽게 띄우게 된 만큼, 사용량 과금 서비스에 기본 지출 상한이 필요하다고 주장했다.

## 가중치 공개

**1조 매개변수 모델의 가중치가 공개를 앞두고 있다.** 가중치는 모델이 학습으로 얻은 수치이고, 이를 누구나 내려받게 푼 모델을 공개 가중치 모델이라 한다. [Mistral](https://mistral.ai/news/mistral-large-4/)은 10월 6일 전체 매개변수 1조 개 가운데 520억 개가 활성화되는 Mistral Large 4를 내놓고, 가중치를 이달 말까지 공개하겠다고 밝혔다. 유럽의 자체 데이터센터에서 엔비디아 GPU 3,800장으로 처음부터 학습했다는 것이 회사의 설명이다.

[Reflection AI](https://reflection.ai/blog/introducing-beam)도 5,010억 매개변수의 Beam을 내놨다. 매번 230억 개만 쓰는 전문가 혼합(MoE) 구조이고, 가중치는 Apache 2.0 라이선스로 이달 하순 공개하는데 지금은 대기 명단으로만 쓸 수 있다.

**엔비디아는 이 회사에 돈을 더 넣으려 한다는 보도가 나왔다.** [SiliconANGLE](https://siliconangle.com/2026/10/11/nvidia-reportedly-in-early-talks-to-buy-acqui-hire-or-invest-more-in-reflection-ai/)이 전한 FT 보도로는 엔비디아가 Reflection AI를 사들이거나 투자를 늘리는 초기 협상을 하고 있다. 엔비디아는 이미 8억 달러를 투자했고, 두 회사는 협상에 대해 공개적으로 논평하지 않았다.

**가중치가 풀려도 쓰는 조건은 라이선스가 정한다.** [the decoder](https://the-decoder.com/alibabas-open-weight-qwen-image-2-1-claims-to-beat-closed-models-in-image-generation-with-just-7-billion-parameters/)에 따르면 알리바바가 9월 20일 낸 이미지 모델 Qwen-Image-2.1은 가중치를 공개했지만 연구용 라이선스라, 상업적으로 쓰려면 따로 허가를 받아야 한다.

## 보안

**[구글](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)은 Gemini 4 Argon을 사이버 방어자에게 먼저 풀었다.** 9월 30일 새 모델을 'Fairwind 프로그램'의 신뢰할 수 있는 사이버 방어자들에게 먼저 배포하고 유료 API 고객과 Google AI Ultra 구독자로 넓힌다고 밝혔으며, 미국 정부의 자발적 출시 전 모델 접근 절차에도 참여하고 있다.

**[OpenAI](https://deploymentsafety.openai.com/gpt-6-october)는 GPT-6를 사이버보안과 생물·화학 분야에서 'High' 역량으로 다룬다고 밝혔다.** 10월 7일 GPT-6를 ChatGPT 전 이용자에게 넓히면서 낸 배포 안전 문서의 내용으로, AI 자기개선 분야는 High 기준에 미치지 않았다고 했다. [포천](https://fortune.com/2026/09/24/openai-launching-gpt-6-cyber-model-and-security-product-devday/)은 OpenAI가 보안 특화 모델 GPT-6 Cyber를 준비하고 있다고 소식통을 인용해 보도했고, OpenAI의 입장은 확인되지 않았다.

**[Anthropic](https://www.anthropic.com/news/cyber-verification-program)은 보안 전문가용 접근을 세 단계로 나눴다.** 10월 6일 사이버 검증 프로그램을 방어 업무용, 승인된 모의해킹까지 더한 레드팀용, 검증된 일부 기관에 한정한 특수용으로 나눴고, 8일에는 참여를 신청한 오픈소스 프로젝트에 무료 보안 점검을 해 주는 [핵심 기반시설 방어 프로그램](https://www.anthropic.com/news/anthropic-cyber-mission)을 내놨다.

**공격하는 쪽에서도 AI 도구의 흔적이 나왔다.** [이투데이](https://www.etoday.co.kr/news/view/2632359)에 따르면 4일 금융당국은 국내 금융사 7곳의 침해 사고에서 같은 공격자의 IP가 여러 곳에서 발견됐고, 공격자는 AI 도구로 여러 금융사를 자동화된 방식으로 공격한 것으로 보인다고 밝혔다. 고객 서비스 영향이나 금전 피해는 없는 것으로 파악됐다. 또 금융보안 관계자에 따르면 공격 IP에서 깃허브에 공개된 AI 기반 자율 침투테스트 도구의 흔적이 확인돼 경찰청 사이버수사국이 조사하고 있다.

**해설:** 세 회사 모두 새 모델의 보안 쪽 능력을 일반 공개와 따로 다뤘는데, 누구에게 먼저, 어디까지 쓰게 할지를 회사가 정하는 방식이다. 한편 같은 시기 국내에서는 누구나 내려받을 수 있는 AI 도구가 공격에 쓰인 정황이 나왔다.

## 주가와 기업 계약

**AI 회사의 매출 보도에 반도체 주가가 내렸다.** [뉴스핌](https://www.newspim.com/news/view/20261009000017)은 OpenAI의 연환산 매출이 그동안 알려진 것보다 200억 달러 적은 500억 달러라는 FT 보도가 반도체 매도로 이어졌다고 전했고, 8일(현지) 필라델피아 반도체지수는 3.39%, 엔비디아는 2.24% 내렸다.

**AI 계약 소식에 주가가 뛴 회사도 있다.** [24/7 Wall St.](https://247wallst.com/investing/2026/09/25/akamai-surges-15-on-11-6b-anthropic-cloud-deal-coreweave-and-cloudflare-tick-up/)는 9월 25일 Anthropic이 Akamai와 7년 116억 달러 규모 클라우드 계약을 맺었다고 전했고, 그날 장중 Akamai 주가는 15% 올라 있었다.

**칩 쪽 회사들은 돈을 풀고 손을 잡았다.** [엔비디아](https://nvidianews.nvidia.com/news/nvidia-announces-a-150-billion-share-repurchase-authorization-increase) 이사회는 자사주 매입 한도를 1,500억 달러 늘려 남은 한도를 2,350억 달러로 만들었다. 반도체 설계 소프트웨어 회사 [시놉시스](https://news.synopsys.com/2026-09-30-OpenAI-and-Synopsys-Announce-GPT-Synopsys-Frontier-Intelligence-to-Revolutionize-Chip-Design)는 OpenAI와 수익 공유를 포함한 다년 계약을 맺고 칩 설계 도구를 직접 다루는 모델 GPT-Synopsys를 발표했지만, 출시 시점은 밝히지 않았다.

## AI 소식을 읽는 세 가지

- **성능 수치는 누가 쟀는지부터 본다.** 이 기간 나온 점수 대부분은 회사가 스스로 잰 것이라, 외부 측정이 나오기 전까지는 회사의 주장으로 읽는다.
- **'공개'가 무엇을 연다는 말인지 본다.** 앱에 넣는 것, API로 파는 것, 가중치를 내려받게 하는 것은 서로 다르고, 가중치는 공개 예정일과 라이선스를 함께 본다.
- **값은 입력과 출력을 따로 본다.** 이번 표의 모델들은 출력 값이 입력의 3~5배라, 답을 길게 쓰게 하는 일일수록 출력 값이 비용을 정한다.

## 다음에 볼 것

- **가중치가 예고대로 풀리는지.**
  [Mistral](https://mistral.ai/news/mistral-large-4/)은 Mistral Large 4의 가중치를 이달 말까지, [Reflection AI](https://reflection.ai/blog/introducing-beam)는 Beam의 가중치를 이달 하순 Apache 2.0 라이선스로 공개하겠다고 밝혔다.
  두 회사의 발표 페이지에 가중치를 내려받는 주소와 라이선스가 올라오는지 본다.
  예고대로 올라오면 이 급의 모델을 누구나 내려받아 쓰게 되는 것이고, 미뤄지면 당분간 회사 API로만 쓰는 것이다.
- **TSMC 실적에서 반도체 쪽 숫자가 어떻게 나오는지.**
  [뉴스핌](https://www.newspim.com/news/view/20261009000017)에 따르면 OpenAI 매출 보도 뒤 8일 반도체지수는 3.39% 내렸고, [TSMC](https://investor.tsmc.com/english/quarterly-results)는 15일 15:00(한국 시간) 3분기 실적 설명회를 연다. 직전 [2분기 매출](https://pr.tsmc.com/english/news/3326)은 402억 달러였다.
  3분기 매출을 2분기 402억 달러와 견준다.
  늘었으면 칩을 만드는 쪽 숫자는 꺾이지 않은 것이고, 줄었으면 매출 보도로 흔들린 반도체 주가에 실적 쪽 근거가 더해지는 것이다.
