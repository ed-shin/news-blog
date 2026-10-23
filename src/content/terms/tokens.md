---
name: "토큰과 토큰당 가격"
title: "AI 토큰이란? 뜻과 100만 토큰당 가격 읽는 법"
description: "AI 언어 모델이 글을 읽고 쓰는 조각이다. 단어보다 작고, AI 회사는 이 조각 수로 값을 매긴다. 값은 100만 토큰당으로, 입력과 출력을 따로 매긴다."
category: "테크"
aliases: ["100만 토큰", "입력 토큰", "출력 토큰", "토큰 가격"]
related: ["ai-agent", "open-weights"]
pubDate: 2026-10-12
updatedDate: 2026-10-23
corrections:
  - date: 2026-10-23
    text: "본문 문장을 이어 쓰고 출처를 문장 끝 괄호 대신 기관 이름에 걸었다. 사실과 숫자는 바꾸지 않았다."
---

## 한 줄로 말하면

**AI 언어 모델이 글을 읽고 쓰는 조각이다.** [구글](https://ai.google.dev/gemini-api/docs/tokens)에 따르면 단어보다 작은 단위이고, AI 회사는 모델이 읽고 쓴 토큰 수로 값을 매긴다.

## 어떻게 세나

**글을 자주 나오는 조각으로 자른다.** [OpenAI](https://developers.openai.com/api/docs/concepts)는 "tokenization"이라는 단어가 "token"과 "ization" 두 토큰으로 나뉘고, "the" 같은 짧은 단어는 한 토큰이라고 설명한다. [구글](https://ai.google.dev/gemini-api/docs/tokens)은 Gemini 모델에서 토큰 하나가 영어 약 4글자이고, 100토큰이 영어 단어 60~80개쯤이라고 밝힌다.

**한국어는 같은 내용에 토큰이 더 든다.** [Petrov 외(NeurIPS 2023)](https://arxiv.org/abs/2305.15425)가 같은 문장을 여러 언어로 옮겨 토큰 수를 잰 연구에서 언어 사이 차이가 최대 15배까지 났고, 연구진은 차이가 큰 언어의 예로 한국어를 들었다. 이 연구의 자료로 보면 2023년 GPT-4 토큰 분할기에서 한국어는 같은 내용의 영어보다 토큰이 약 2.4배 들었다.

## 값은 어떻게 매기나

**100만 토큰당 값으로, 입력과 출력을 따로 매긴다.** OpenAI와 구글 모두 가격표를 100만 토큰당 값으로 적는데, 2026년 10월 12일 기준 [OpenAI](https://developers.openai.com/api/docs/pricing)의 GPT-6.1 Sol은 입력 2달러, 출력 10달러다. 또 [구글](https://ai.google.dev/gemini-api/docs/pricing)은 모델이 답하기 전에 생각하는 데 쓴 토큰도 출력으로 센다.

예를 들어 질문과 자료로 2,000토큰을 보내고 답으로 500토큰을 받으면, GPT-6.1 Sol 기준으로 입력과 출력 값을 따로 셈해 더한다.

1. 입력: 2,000 × 2달러 ÷ 100만 = 0.004달러
2. 출력: 500 × 10달러 ÷ 100만 = 0.005달러
3. 합계: 0.009달러

출력 토큰이 입력의 4분의 1인데도 값은 출력 쪽이 더 크다.

## 왜 보나

**AI 회사의 가격 경쟁이 토큰 값으로 드러난다.** 2026년 9~10월에는 OpenAI가 GPT-6 Sol의 값을 직전 모델의 절반으로 매기는 등 같은 급 모델의 값이 크게 내렸다([AI 모델 출시·가격·가중치 공개](/jogan/feature/ai-models-three-weeks/)). 토큰 값은 AI를 쓰는 회사의 비용이자, AI를 파는 회사의 매출 단가다.

## 숫자는 이렇게 읽는다

- **입력과 출력을 따로 본다.** 2026년 9~10월에 나온 주요 모델은 출력 값이 입력의 3~5배였다. 답을 길게 쓰게 하는 일일수록 출력 값이 비용을 정한다.
- **캐시 값이 따로 있다.** 같은 앞부분을 되풀이해 보내면 싸게 매기는 값이다. 예를 들어 [OpenAI](https://developers.openai.com/api/docs/pricing)의 GPT-6.1 Sol은 캐시된 입력이 100만 토큰당 0.10달러로, 일반 입력 2달러의 20분의 1이다.
- **한국어로 쓰면 같은 일에 토큰이 더 들 수 있다.** 다만 위 연구는 2023년 토큰 분할기로 잰 것이라, 새 모델의 분할기에서는 차이가 다를 수 있다.
- **값은 날짜와 함께 본다.** 회사들이 값을 자주 바꾸고 할인 기간을 따로 둔다. 조간은 값을 적을 때 발표일이나 확인한 날을 함께 적는다.

## 출처

- [구글 — Gemini 토큰 이해하기](https://ai.google.dev/gemini-api/docs/tokens): 토큰 하나 ≈ 영어 4글자, 100토큰 ≈ 영어 단어 60~80개, 토큰 수로 매기는 값
- [OpenAI — API 핵심 개념](https://developers.openai.com/api/docs/concepts): 단어가 토큰으로 나뉘는 예
- [OpenAI — API 가격](https://developers.openai.com/api/docs/pricing): 100만 토큰당 가격, GPT-6.1 Sol 입력·캐시·출력 값(2026년 10월 12일 확인)
- [구글 — Gemini API 가격](https://ai.google.dev/gemini-api/docs/pricing): 100만 토큰당 가격, 생각에 쓴 토큰을 출력으로 세는 방식
- [Petrov 외, "언어 모델 토큰 분할기가 언어 사이에 만드는 불공평"(NeurIPS 2023)](https://arxiv.org/abs/2305.15425): 언어 사이 토큰 수 차이 최대 15배, 한국어 사례
