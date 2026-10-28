---
title: "AI 모델 출시 — 10월 14~28일"
description: "10월 14일부터 28일까지 DeepSeek, 문샷AI, OpenAI가 AI 모델을 하나씩 새로 냈다. DeepSeek V4.1 Flash 1017, Kimi K3.1 Pro, GPT-6.1 Terra를 발표일·쓸 수 있는 곳·값·가중치 공개 여부로 나란히 놓고, OpenAI가 Terra를 사이버보안 'Critical'로 다룬다는 회사 판정의 뜻과 외부 기관의 평가를 측정 조건과 함께 정리했다."
pubDate: 2026-10-29
tags: ["기획", "테크"]
period: { from: 2026-10-14, to: 2026-10-28 }
highlights:
  - { label: "다룬 모델", value: "3개", note: "DeepSeek·문샷AI·OpenAI, 10/17~10/26 발표" }
  - { label: "100만 토큰당 출력 값", value: "$1.20~$10", note: "DeepSeek·OpenAI·문샷AI API" }
  - { label: "가중치 공개", value: "1개", note: "DeepSeek(MIT), Kimi는 11월 4일까지 예정" }
---

## 먼저 요점만

1. **10월 17일부터 26일 사이 DeepSeek, 문샷AI, OpenAI가 모델을 하나씩 새로 냈다.** DeepSeek V4.1 Flash 1017, Kimi K3.1 Pro, GPT-6.1 Terra이고, 100만 토큰당 출력 값은 1.20달러, 10달러, 5달러다. 가중치를 내려받을 수 있는 것은 MIT 라이선스로 푼 DeepSeek 하나이고, 문샷AI는 11월 4일까지 풀겠다고 했다.
2. **OpenAI는 Terra를 사이버보안에서 'Critical'로 다룬다고 밝혔다.** OpenAI가 자체 위험 기준의 두 단계 가운데 위 단계로 내린 판정이고, 외부 기관이 매긴 등급은 아니다. DeepSeek와 문샷AI의 발표와 모델 카드에는 이런 등급이 없다.
3. **27일 외부 평가의 판이 바뀌자 같은 모델의 점수가 달라졌다.** Artificial Analysis가 지능 지수를 5판으로 바꾸면서 Kimi K3.1 Pro는 55에서 46이 됐다. 점수는 어느 판, 어떤 설정에서 쟀는지와 함께 봐야 한다.

9월 1일~10월 13일에 나온 모델은 [OpenAI·Anthropic·Google 9~10월 새 모델 출시](/jogan/feature/ai-models-september-october/)에 정리했다. 이 글은 그 뒤 조간 일일 글에 실린 범용 모델 셋을 같은 항목으로 다루고, 음성 모델 묶음인 미스트랄의 Voxtral 3([10월 21일 일일](/jogan/daily/2026-10-21/#tech))처럼 음성·이미지 전용 모델은 뺐다.

## 한눈에 보는 세 모델

**세 모델은 값과 가중치 공개에서 갈린다.** 토큰은 모델이 글을 처리하는 단위이고, 가중치는 학습으로 정해진 모델의 수치라 공개되면 내려받아 직접 돌리거나 고칠 수 있지만, 필요한 장비와 허용 범위는 모델과 라이선스마다 다르다. 값은 앱 구독료가 아니라 다른 프로그램에서 모델을 불러 쓰는 API의 사용료이고, 세 회사 모두 같은 입력을 반복해 보내면 그 부분에는 더 낮은 캐시 값을 받으므로 표에는 캐시되지 않은 입력 값을 적었다. 위험 등급 칸에는 회사가 자체 기준으로 매겨 발표한 것만 적었다.

| 발표(현지) | 회사 | 모델 | 쓸 수 있는 곳 | 100만 토큰당 값(캐시 안 된 입력/출력) | 가중치 | 회사가 밝힌 위험 등급 |
|---|---|---|---|---|---|---|
| 10월 17일 | DeepSeek | V4.1 Flash 1017 | DeepSeek 웹·앱, API | $0.30 / $1.20(평일 혼잡 시간 밖은 절반) | 공개(MIT 라이선스) | 발표 없음 |
| 10월 24일 | 문샷AI | Kimi K3.1 Pro | Kimi.ai·앱, Kimi Work, Kimi Code, API | $2 / $10 | 11월 4일까지 공개 예정 | 발표 없음 |
| 10월 26일 | OpenAI | GPT-6.1 Terra | ChatGPT Work·Codex(Plus·Pro·Enterprise·Edu), API | $1 / $5 | 비공개 | 사이버보안 Critical, 생물·화학 High |

*발표일은 회사 소재지 기준이다. DeepSeek 출시일과 이용처는 [출시문](https://api-docs.deepseek.com/news/news261017/)에 있다. Kimi K3.1 Pro는 베이징 시간 24일 새벽 1시 15분(협정 세계시 23일 17시 15분)에 발표됐다. DeepSeek 값은 평일 혼잡 시간(한국 시간 10~13시, 15~19시) 기준이다. Terra는 입력이 27만 2,000토큰을 넘으면 그 요청 전체에 입력 2배·출력 1.5배 값을 받는다. 출처: [DeepSeek 변경 기록](https://api-docs.deepseek.com/updates)·[가격표](https://api-docs.deepseek.com/quick_start/pricing)·[모델 카드](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017), [Kimi K3.1 Pro 발표](https://www.kimi.ai/blog/kimi-k3-1-pro)·[가격표](https://platform.kimi.ai/docs/pricing/chat)·[발표 시각](https://x.com/Kimi_Moonshot/status/2113680701770068067), [GPT-6.1 Terra 발표](https://openai.com/index/introducing-gpt-6-1-terra/)·[API 문서](https://developers.openai.com/api/docs/models/gpt-6.1-terra)·[안전 문서](https://deploymentsafety.openai.com/gpt-6-1-terra).*

## 10/17 — DeepSeek V4.1 Flash 1017

**[DeepSeek](https://api-docs.deepseek.com/news/news261017/)는 17일 V4.1 Flash를 새 판 1017로 바꾸고, 가중치를 MIT 라이선스로 공개했다.** 9월 10일 낸 V4.1 Flash를 고친 판으로 웹과 앱, API에 바로 나왔고, [변경 기록](https://api-docs.deepseek.com/updates)에 따르면 API 호출 방법과 값은 그대로다. [허깅페이스 모델 카드](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)는 이를 V4.1 Flash의 작은 업데이트라고 부르며, 작업 시간과 출력 길이를 줄여 같은 일을 더 적은 비용으로 끝낼 수 있다고 적었다.

가중치는 매개변수 약 7,630억 개 규모로 [허깅페이스](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)에서 내려받을 수 있고, MIT 라이선스는 상업적 사용과 수정·재배포를 허용한다. API 값은 [DeepSeek 가격표](https://api-docs.deepseek.com/quick_start/pricing)에서 100만 토큰당 입력 0.30달러·출력 1.20달러인데, 평일 혼잡 시간의 값이고 그 밖의 시간과 주말·중국 공휴일에는 절반이다.

## 10/24 — Kimi K3.1 Pro

**[문샷AI](https://www.kimi.ai/blog/kimi-k3-1-pro)는 24일(베이징 시간) Kimi K3.1 Pro를 내놓고, 전체 가중치는 11월 4일까지 공개하겠다고 밝혔다.** Kimi K3를 더 많은 연산으로 후속 학습한 K3.1 시리즈의 첫 모델이고, [문샷AI](https://x.com/Kimi_Moonshot/status/2113680701770068067)에 따르면 전체 매개변수 2조 8,000억 개 가운데 한 번에 1,040억 개만 쓰는 전문가 혼합(MoE) 구조다.

같은 날부터 Kimi.ai와 모바일 앱, 데스크톱 앱 Kimi Work, 코딩 도구 Kimi Code, API에서 쓸 수 있고, 회사가 2~3배 빠르다고 한 Highspeed 판도 함께 나왔다. [Kimi API 가격표](https://platform.kimi.ai/docs/pricing/chat)로 100만 토큰당 입력 2달러·출력 10달러여서 직전 Kimi K3(3달러·15달러)보다 3분의 1 낮고, Highspeed는 4달러·20달러다. 가중치는 28일까지 [허깅페이스](https://huggingface.co/moonshotai) 문샷AI 저장소에 올라오지 않았고, 공개할 때 붙일 라이선스도 밝히지 않았다.

## 10/26 — GPT-6.1 Terra

**[OpenAI](https://openai.com/index/introducing-gpt-6-1-terra/)는 26일 GPT-6.1 Terra를 GPT-6.1 Sol의 절반 값에 내놨다.** 이미지를 읽고 판단하는 일과 컴퓨터 조작, 글쓰기를 빠르고 효율적으로 하도록 만든 모델로 GPT-5.6 Terra의 뒤를 잇는다. 회사는 들어온 청구서를 읽어 회계 소프트웨어에 옮기는 것 같은 대량 업무를 용도로 들었고, 가장 복잡한 코딩에는 GPT-6.1 Sol과 GPT-6 Astra가 여전히 낫다고 적었다.

ChatGPT Work와 Codex에서는 Plus·Pro·Enterprise·Edu 이용자가 쓸 수 있고, API 값은 100만 토큰당 입력 1달러·출력 5달러다. [OpenAI API 문서](https://developers.openai.com/api/docs/models/gpt-6.1-terra)에 따르면 문맥 한도는 105만 토큰이고 글과 이미지를 받으며, 입력이 27만 2,000토큰을 넘는 요청은 전체에 입력 2배·출력 1.5배 값을 받는다. 가중치는 공개하지 않았다.

## 위험 등급

**Terra의 'Critical'은 OpenAI가 자기 기준으로 내린 판정이다.** [OpenAI 발표](https://openai.com/index/introducing-gpt-6-1-terra/)는 Terra가 자체 대비 체계(Preparedness Framework)에서 사이버보안의 Critical 기준에 이르렀다고 했고, [안전 문서](https://deploymentsafety.openai.com/gpt-6-1-terra)는 GPT-6 Astra 때처럼 Terra를 사이버보안에서 Critical, 생물·화학에서 High 역량으로 다룬다고 적었다. AI 연구를 AI가 스스로 앞당기는 자기개선 영역은 High에 이르지 않았다고 봤다.

[OpenAI](https://openai.com/index/updating-our-preparedness-framework/)가 2025년 4월 고친 대비 체계는 위험한 능력을 두 단계로 나눈다. High는 심각한 피해로 가는 기존 경로를 키울 수 있는 수준이고 Critical은 전에 없던 새 경로를 열 수 있는 수준인데, Critical에 이른 모델은 배포 전뿐 아니라 개발 중에도 위험을 줄일 안전장치를 갖춰야 한다.

[안전 문서](https://deploymentsafety.openai.com/gpt-6-1-terra)는 사이버보안의 Critical을 사람 개입 없이 방어가 단단한 실제 핵심 시스템 여러 곳에서 작동하는 모든 심각도의 제로데이(아직 알려지지 않아 패치가 없는 취약점) 공격 코드를 찾아 만들거나, 큰 목표만 받고도 새 공격 전략을 처음부터 끝까지 짜서 실행할 수 있는 모델로 정의한다. 이 판정에 따라 Terra에도 GPT-6.1 Sol·Astra와 같은 안전장치를 쓰는데, 안전 문서는 그 내용을 GPT-6 Astra의 시스템 카드로 넘기고, 사이버 능력이 커지는 만큼 방어 목적의 이용자에게 접근을 넓히는 일과 안전장치를 함께 늘린다는 원칙을 적었다. 또 공개하지 않은 내부 안전장치 보고서를 바탕으로 안전 자문 그룹이 권고하고 경영진이 이 안전장치로 출시해도 된다고 판단했다고 밝혔다.

반면 DeepSeek와 문샷AI의 발표에는 이런 등급이 없다. [문샷AI](https://www.kimi.ai/blog/kimi-k3-1-pro)는 대신 가중치 공개를 앞두고 중간 학습과 강화학습 단계에서 사이버 관련 데이터를 뺐다고 밝히고, 사이버 공격 능력의 최전선을 넓히는 가중치는 공개하지 않는다는 원칙을 내걸었다. K3.1 Pro의 사이버 능력은 출시된 지 석 달 넘은 비공개 최첨단 모델에도 못 미친다는 것이 회사의 설명이다. [DeepSeek](https://api-docs.deepseek.com/updates)의 변경 기록과 [모델 카드](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)에는 위험 평가나 등급이 없다.

**해설:** 세 회사가 위험을 밝히는 방식이 달라 등급끼리 견줄 수 없다. Critical은 OpenAI가 자기 체계로 내린 판정이어서, 등급을 내지 않은 회사의 모델이 더 안전하다는 뜻도, Critical이 붙은 모델이 다른 회사 모델보다 위험하다는 뜻도 아니다.

## 외부 평가

**Artificial Analysis가 27일 지능 지수를 5판으로 바꾸자, 같은 모델의 점수가 하루 사이 달라졌다.** 아래는 회사가 아닌 Artificial Analysis, Vals, ARC Prize가 직접 잰 결과다.

| 모델 | Artificial Analysis 지능 지수(4.3판) | Artificial Analysis 지능 지수(5판) | Vals 지수 2.2판 | ARC-AGI-2 |
|---|---|---|---|---|
| DeepSeek V4.1 Flash 1017 | 45 | 32 | 61.26% ±1.05 | 78.1% |
| Kimi K3.1 Pro | 55 | 46 | 62.52% ±1.14 | — |
| GPT-6.1 Terra | 48 | — | 60.17% ±1.03 | — |

- **Artificial Analysis 지능 지수:** 여러 평가를 묶은 점수다. 4.3판은 그 전까지 쓰던 판이고, 27일 나온 5판은 평가 아홉 개를 지식 업무·코딩·과학·일반에 25%씩 나눠 묶었으며 60%를 문제나 답을 공개하지 않은 시험으로 잰다. DeepSeek와 Terra는 가장 높은 추론 설정(max)에서 쟀고 Kimi는 설정 표기가 없다([Kimi 4.3판](https://artificialanalysis.ai/articles/kimi-k3-1-pro-launch-benchmarks), [DeepSeek 4.3판](https://web.archive.org/web/20261026042325/https://artificialanalysis.ai/models/deepseek-v4-1-flash-1017), [Terra 4.3판](https://web.archive.org/web/20261026185011/https://artificialanalysis.ai/models/gpt-6-1-terra), [5판 발표](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5)). 5판 점수는 발표 글에 실린 것만 적었다.
- **설정과 오차:** max는 모델이 답하기 전에 가장 오래 추론하게 하는 설정이고, ± 뒤의 표준오차는 점수가 표본에 따라 흔들릴 수 있는 폭이다.
- **Vals 지수:** 금융·코딩·법률·세무 업무에서 AI가 여러 단계를 해내는 능력을 재고, 미국 경제에서 각 분야가 차지하는 비중대로 점수를 합친다. 10월 19일 나온 2.2판이고, 세 모델 모두 max 설정이며 ±는 표준오차다([Vals](https://web.archive.org/web/20261027221121/https://www.vals.ai/benchmarks/vals_index), [DeepSeek](https://www.vals.ai/models/deepseek_deepseek-v4.1-flash-1017)·[Kimi](https://www.vals.ai/models/kimi_kimi-k3.1-pro)·[Terra](https://www.vals.ai/models/openai_gpt-6.1-terra)).
- **ARC-AGI-2:** 처음 보는 퍼즐의 규칙을 찾아내는 시험이다. [ARC Prize](https://x.com/arcprize/status/2113318031954764273)가 22일 비공개 시험 세트(Semi-Private)로 검증해 낸 DeepSeek의 max 설정 점수이고, Terra와 Kimi의 결과는 28일까지 나오지 않았다([결과](https://arcprize.org/results/deepseek-v4-1-flash-1017)).

5판은 새 평가 둘(FrontierCode 2.0, Terminal-Bench-Science)을 넣고 GDPval-AA·SciCode·AA-LCR을 뺐는데, 공개 가중치 모델과 비공개 모델의 거리도 이 판에서 달라졌다. [Artificial Analysis](https://artificialanalysis.ai/articles/kimi-k3-1-pro-launch-benchmarks)는 Kimi 출시 당일, 4.3판에서 공개 가중치 모델 1위와 비공개 모델 1위의 차이가 12점인데 Kimi 가중치가 풀리면 3점으로 준다고 했다. 그런데 Kimi를 넣어 다시 잰 [5판](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5)에서는 그 차이가 12점이었다. [10월 24일 일일](/jogan/daily/2026-10-24/#tech)에 실은 55점과 '3점'은 4.3판 기준이고, [직전 기획](/jogan/feature/ai-models-september-october/)에 실은 점수(9월 7일 바뀐 판)도 5판 점수와 바로 견줄 수 없다.

같은 판 안에서도 설정에 따라 점수가 갈린다. [ARC Prize 결과](https://arcprize.org/results/deepseek-v4-1-flash-1017)를 보면 DeepSeek는 max에서 78.1%였지만, high(68.6%)는 오히려 low(73.6%)보다 낮았다.

[Vals](https://web.archive.org/web/20261027221121/https://www.vals.ai/benchmarks/vals_index) 지수 시험을 한 번 치르는 데 든 값도 모델마다 달라서, DeepSeek 0.66달러, Terra 2.92달러, Kimi 6.44달러였다.

## 다음에 볼 것

- **11월 4일까지 Kimi K3.1 Pro 가중치가 풀리는지.**
  [문샷AI](https://www.kimi.ai/blog/kimi-k3-1-pro)는 전체 가중치를 11월 4일까지 공개하겠다고 했지만 라이선스는 밝히지 않았고, 가중치는 28일까지 [허깅페이스](https://huggingface.co/moonshotai) 문샷AI 저장소에 올라오지 않았다.
  11월 4일까지 이 저장소에 K3.1 Pro가 올라오는지, 붙은 라이선스가 무엇인지 보면 된다.
  올라오면 이 기간 모델 가운데 가중치를 내려받을 수 있는 것이 둘이 되고, 라이선스가 상업적으로 쓸 수 있는 범위를 정한다. 올라오지 않으면 Kimi의 가중치 공개는 아직 약속으로 남는다.
- **ARC Prize가 Terra와 Kimi K3.1 Pro의 결과를 내는지.**
  [ARC Prize](https://x.com/arcprize/status/2113318031954764273)는 22일 DeepSeek V4.1 Flash 1017의 ARC-AGI-2 결과를 냈지만, Terra와 Kimi K3.1 Pro의 결과는 28일까지 없다.
  ARC Prize 결과 페이지에 두 모델이 오르는지, 어떤 추론 설정으로 검증했는지 보면 된다.
  오르면 세 모델을 같은 시험의 같은 검증 세트로 나란히 놓을 수 있고, 오르지 않으면 ARC-AGI-2에서는 세 모델을 함께 견줄 수 없고, 셋을 나란히 놓을 수 있는 외부 평가는 Artificial Analysis 4.3판과 Vals로 남는다.
