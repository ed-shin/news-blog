---
name: "AI 에이전트"
title: "AI 에이전트란? 챗봇과 다른 점, 움직이는 방식과 위험"
description: "목표를 받으면 스스로 계획을 세우고 도구를 써서 실제로 일을 해 내는 AI 시스템이다. 모델에 도구를 붙이고, 정한 조건이 될 때까지 판단과 행동을 되풀이한다."
category: "테크"
aliases: ["AI 에이전트", "코딩 에이전트", "에이전트"]
related: ["harness", "tokens", "open-weights"]
pubDate: 2026-10-12
updatedDate: 2026-10-23
corrections:
  - date: 2026-10-23
    text: "본문 문장을 이어 쓰고 출처를 문장 끝 괄호 대신 기관 이름에 걸었다. 사실과 숫자는 바꾸지 않았다."
---

## 한 줄로 말하면

**목표를 받으면 스스로 계획을 세우고 도구를 써서 실제로 일을 해 내는 AI 시스템이다.** [미국 국립표준기술연구소(NIST)](https://www.federalregister.gov/documents/2026/01/08/2026-00206/request-for-information-regarding-security-considerations-for-artificial-intelligence-agents)는 AI 에이전트를 계획을 세우고, 실제 시스템이나 환경에 영향을 주는 행동을 스스로 할 수 있는 시스템으로 설명한다.

## 어떻게 움직이나

**모델에 도구를 붙인 구조다.** [NIST](https://www.federalregister.gov/documents/2026/01/08/2026-00206/request-for-information-regarding-security-considerations-for-artificial-intelligence-agents)는 AI 에이전트가 생성형 AI 모델 하나 이상과, 그 모델이 여러 행동을 골라 할 수 있게 도구를 붙여 주는 소프트웨어로 이뤄진다고 설명한다. [OpenAI](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)의 안내서도 에이전트의 기본을 판단하는 모델, 행동에 쓰는 도구, 행동 방식을 정한 지시문 셋으로 나눈다.

이 구조에서 에이전트는 정한 조건이 될 때까지 판단과 행동을 되풀이한다. 모델이 다음에 할 일을 정하고, 도구를 불러 결과를 받고, 그 결과를 보고 다시 정하는 식이다. [OpenAI](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) 안내서에 따르면 이 반복은 특정 결과를 냈거나, 오류가 났거나, 정해 둔 횟수에 닿으면 끝난다.

코딩 에이전트가 좋은 예로, 모델에 코드를 고치고 명령을 실행하는 도구를 붙이고 작업 계획과 컨텍스트(모델이 한 번에 보는 자료)를 관리하는 장치로 감싼다. 이 감싸는 장치를 [하네스](/jogan/terms/harness/)라고 부른다. 2026년 9월 arXiv에 올라온 연구는 하네스를 부품별로 떼어 평가했는데, 부품의 효과는 모델과 조건에 따라 달랐다. 이를테면 계획 기능은 약한 모델에서는 정확도를 받쳐 줬고, 강한 모델에서는 비용을 줄였다([9월 20일 일일](/jogan/daily/2026-09-20/#tech)).

**질문에 답만 하는 챗봇은 에이전트가 아니다.** [OpenAI](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) 안내서는 모델이 작업 흐름을 이끌지 않는 단순한 챗봇은 에이전트가 아니라고 적었고, [NIST](https://www.federalregister.gov/documents/2026/01/08/2026-00206/request-for-information-regarding-security-considerations-for-artificial-intelligence-agents)도 스스로 행동하도록 짜이지 않은 챗봇은 따로 본다.

## 왜 보나

**AI 회사들이 새 제품을 에이전트로 내놓고 있다.** 2026년 9월 말에는 사용자가 정한 목표를 백그라운드에서 계속 수행하는 상시 에이전트가 나왔고([9월 30일 일일](/jogan/daily/2026-09-30/#tech)), 에이전트를 감시·격리하는 참조 설계([9월 30일 일일](/jogan/daily/2026-09-30/#tech))와 웹사이트가 에이전트에게 사용료를 받게 하는 관문([10월 2일 일일](/jogan/daily/2026-10-02/#tech))도 나왔다. 한편 [OECD](https://www.oecd.org/content/dam/oecd/en/publications/reports/2026/02/the-agentic-ai-landscape-and-its-conceptual-foundations_a9d4b451/396cf758-en.pdf)는 여러 에이전트가 일을 나눠 맡아 사람의 감독을 적게 받으며 움직이는 시스템을 '에이전틱 AI'로 부른다.

## 뉴스는 이렇게 읽는다

- **누가 감독하는지 본다.** [NIST](https://www.federalregister.gov/documents/2026/01/08/2026-00206/request-for-information-regarding-security-considerations-for-artificial-intelligence-agents)는 에이전트가 사람의 감독이 거의 없이 배치될 수 있다고 적었다. 사람이 단계마다 승인하는지, 목표만 주고 맡기는지에 따라 위험이 다르다.
- **남이 숨긴 지시에 휘둘릴 수 있다.** [NIST](https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations)는 많은 에이전트가 '에이전트 하이재킹'에 취약하다고 밝혔다. 에이전트가 읽어 들이는 자료에 공격자가 지시를 숨겨 넣어 원치 않는 행동을 하게 만드는 것이다.
- **비용은 반복 횟수만큼 쌓인다.** 에이전트는 판단할 때마다 모델을 다시 불러 [토큰](/jogan/terms/tokens/)을 쓰고, 오래 도는 작업일수록 비용이 커진다.

## 출처

- [NIST — AI 에이전트 보안 의견 요청(2026년 1월, 미 연방관보)](https://www.federalregister.gov/documents/2026/01/08/2026-00206/request-for-information-regarding-security-considerations-for-artificial-intelligence-agents): AI 에이전트의 정의와 구성, 챗봇과의 구분, 낮은 감독
- [NIST — 에이전트 하이재킹 평가(2025)](https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations): 숨긴 지시로 에이전트를 휘두르는 공격
- [OECD — 에이전틱 AI의 지형과 개념(2026년 2월)](https://www.oecd.org/content/dam/oecd/en/publications/reports/2026/02/the-agentic-ai-landscape-and-its-conceptual-foundations_a9d4b451/396cf758-en.pdf): AI 에이전트와 에이전틱 AI의 정의
- [OpenAI — 에이전트 만들기 안내서](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf): 모델·도구·지시문, 끝나는 조건, 챗봇과의 구분
