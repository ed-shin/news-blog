---
name: "공개 가중치(오픈 웨이트)"
title: "오픈 웨이트란? 공개 가중치 모델과 오픈소스 AI의 차이"
description: "AI 모델이 학습으로 얻은 수치(가중치)를 누구나 내려받게 풀어 놓은 모델이다. 학습 코드와 데이터 정보까지 여는 오픈소스 AI와는 다르고, 쓰는 조건은 라이선스가 정한다."
category: "테크"
aliases: ["오픈웨이트", "오픈 웨이트", "공개 가중치", "가중치 공개"]
related: ["ai-agent", "tokens"]
pubDate: 2026-10-12
---

## 한 줄로 말하면

**AI 모델이 학습으로 얻은 수치(가중치)를 누구나 내려받게 풀어 놓은 모델이다.** 미국 상무부 통신정보관리청(NTIA)은 가중치를 인터넷에서 내려받게 하는 식으로 일반에 공개한 모델을 이렇게 부른다([NTIA](https://www.ntia.gov/sites/default/files/publications/ntia-ai-open-model-report.pdf)).

## 무엇을 여는 것인가

**가중치는 모델이 답을 정하는 데 쓰는 수치다.** NTIA는 가중치를 입력에 대해 모델이 내놓을 출력을 정하는 수치로 설명하고, 개발자가 정한 목표에 맞춰 학습하며 얻은 값이라고 적었다. 가중치가 닫힌 모델은 입력을 보내고 답을 받을 수만 있고, 가중치 자체에는 손댈 수 없다([NTIA](https://www.ntia.gov/sites/default/files/publications/ntia-ai-open-model-report.pdf)).

**가중치의 개수가 모델의 크기다.** 흔히 '매개변수'라고 부른다. 2026년 10월 Mistral이 낸 Mistral Large 4는 매개변수가 1조 개다. 다만 전체 가운데 520억 개만 활성화된다. Reflection AI의 Beam은 5,010억 개 가운데 매번 230억 개만 쓰는 전문가 혼합(MoE) 구조다([AI 모델 3주](/jogan/feature/ai-models-three-weeks/)). 매번 전체가 아니라 일부만 계산에 쓰는 방식이다.

**오픈 웨이트와 오픈소스 AI는 다르다.** 오픈소스이니셔티브(OSI)의 '오픈소스 AI 정의 1.0'은 누구나 허락 없이 어떤 목적으로든 쓰고, 들여다보고, 고치고, 나눌 수 있어야 오픈소스 AI라고 본다. 그러려면 가중치뿐 아니라 학습·실행 코드 전부와, 비슷한 모델을 다시 만들 수 있을 만큼 자세한 학습 데이터 정보까지 내놓아야 한다([OSI](https://opensource.org/ai/open-source-ai-definition)). 가중치만 푼 모델은 이 기준에 못 미친다.

## 쓰는 조건은 라이선스가 정한다

- **Apache 2.0:** 누구에게나 사용료 없이 복제·수정·배포를 허락하고, 특허 사용권도 준다([Apache 2.0 원문](https://www.apache.org/licenses/LICENSE-2.0)). OpenAI는 자사 공개 가중치 모델 gpt-oss를 이 라이선스로 내놓으며 상업적 배포에도 맞다고 밝혔다([OpenAI](https://github.com/openai/gpt-oss)). Reflection AI는 Beam의 가중치를 이 라이선스로 공개하겠다고 예고했다([10월 7일 일일](/jogan/daily/2026-10-07/#tech)).
- **연구용 라이선스:** 가중치를 내려받을 수는 있어도 상업적으로 쓰려면 따로 허가가 필요하다. 2026년 9월 알리바바가 낸 이미지 모델 Qwen-Image-2.1이 이랬다([9월 21일 일일](/jogan/daily/2026-09-21/#tech)).
- **조건이 붙은 라이선스:** 메타의 Llama 4 라이선스는 월간 이용자가 7억 명을 넘는 서비스라면 메타에 따로 사용권을 요청해야 한다고 정한다([메타 Llama 4 라이선스](https://raw.githubusercontent.com/meta-llama/llama-models/main/models/llama4/LICENSE)).

## 왜 보나

**회사 API에 묶이지 않고 직접 돌릴 수 있다.** Mistral은 2025년 Apache 2.0으로 낸 모델에 대해, 가중치를 내려받아 자기 장비에 깔 수 있고 어떤 용도로든 고쳐 쓸 수 있다고 밝혔다([Mistral](https://mistral.ai/news/mistral-small-3)). 큰 모델의 가중치가 풀리면 그 급의 모델을 쓰는 비용과 방식이 달라진다.

## 뉴스는 이렇게 읽는다

- **'공개'가 무엇을 연다는 말인지 본다.** 앱에 넣는 것, API로 파는 것, 가중치를 내려받게 하는 것은 다르다.
- **예고와 실제 공개를 가른다.** "이달 말까지 공개한다"는 아직 내려받을 수 없다는 뜻이다. 회사 발표 페이지에 내려받는 주소가 올라왔는지 본다.
- **라이선스를 함께 본다.** 같은 '공개 가중치'라도 상업적으로 쓸 수 있는지, 이용자 수에 조건이 붙는지가 다르다.

## 출처

- [NTIA — 가중치가 널리 공개된 범용 기반 모델 보고서(2024)](https://www.ntia.gov/sites/default/files/publications/ntia-ai-open-model-report.pdf): 가중치와 공개 가중치 모델의 정의, 닫힌 모델과의 차이
- [OSI — 오픈소스 AI 정의 1.0](https://opensource.org/ai/open-source-ai-definition): 쓰고·들여다보고·고치고·나눌 자유, 데이터 정보·코드·가중치 요건
- [Apache 라이선스 2.0](https://www.apache.org/licenses/LICENSE-2.0): 복제·수정·배포 허락과 특허 사용권
- [OpenAI — gpt-oss](https://github.com/openai/gpt-oss): Apache 2.0으로 낸 공개 가중치 모델
- [메타 — Llama 4 라이선스](https://raw.githubusercontent.com/meta-llama/llama-models/main/models/llama4/LICENSE): 월간 이용자 7억 명 조건
- [Mistral — Mistral Small 3(2025)](https://mistral.ai/news/mistral-small-3): 내려받아 직접 배포하고 고쳐 쓸 수 있다는 설명
