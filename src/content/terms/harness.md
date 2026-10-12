---
name: "하네스(에이전트 하네스)"
title: "AI 하네스란? 모델에게 손발을 달아 주는 틀, 예시로 보기"
description: "AI 모델이 내놓은 '이걸 하겠다'는 글자를 실제 행동으로 옮기고, 그 결과를 다시 모델에게 돌려주는 소프트웨어다. 같은 모델도 어떤 하네스에서 돌리느냐에 따라 결과와 비용이 달라진다."
category: "테크"
aliases: ["하네스"]
related: ["ai-agent", "mcp", "tokens"]
pubDate: 2026-10-12
---

## 한 줄로 말하면

**AI 모델이 내놓은 '이걸 하겠다'는 글자를 실제 행동으로 옮겨 주는 소프트웨어다.** 모델은 글자만 내놓을 뿐, 직접 파일을 열거나 명령을 실행하지 못한다. 구글은 모델이 도구를 직접 실행하지 않으며, 실행은 모델을 부르는 프로그램이 맡고 그 결과를 다시 모델에게 보낸다고 설명한다. 이 과정은 여러 번 되풀이될 수 있다([구글](https://ai.google.dev/gemini-api/docs/function-calling)). 이 일을 맡는 틀이 하네스이고, 모델과 하네스를 합친 것이 [AI 에이전트](/jogan/terms/ai-agent/)다.

## 버그 하나 고치기로 보면

사용자가 "이 버그를 고쳐 줘"라고 맡긴 경우다.

1. 하네스가 과제와 함께 "파일 읽기, 파일 고치기, 명령 실행을 쓸 수 있다"는 도구 목록을 모델에게 보낸다.
2. 모델이 "a.py를 읽고 싶다"고 답한다. 하네스가 실제로 파일을 읽어 내용을 돌려준다.
3. 모델이 "12번째 줄을 이렇게 고쳐라"라고 하면 하네스가 파일을 고친다.
4. 모델이 "테스트를 돌려라"라고 하면 하네스가 돌리고, 실패 메시지를 돌려준다.
5. 2~4를 되풀이한다. 기록이 길어져 모델이 한 번에 볼 수 있는 양을 넘으려 하면, 하네스가 오래된 기록을 덜어 내거나 요약한다.
6. 테스트가 통과하거나 정해 둔 횟수에 닿으면 멈춘다.

**같은 요리사도 주방에 따라 달라진다.** 요리사가 모델이라면 하네스는 주방이다. 어떤 칼과 오븐을 갖췄는지(도구), 레시피를 먼저 짜는지(계획), 좁은 작업대에서 다 쓴 재료를 어떻게 치우는지(기록 관리)가 같은 요리사의 속도와 재료비를 바꾼다.

## 하네스는 어디에 있나

**AI 코딩 도구가 대표적인 하네스다.** Anthropic의 Claude Code와 OpenAI의 Codex CLI는 모두 코드를 읽고, 파일을 고치고, 명령을 실행한다([Anthropic](https://code.claude.com/docs/en/overview), [OpenAI](https://learn.chatgpt.com/docs/codex/cli)). Cursor 같은 편집기도 여러 회사의 모델을 받아 쓰는 하네스다. xAI는 Grok 4.7을 Cursor와 외부 코딩 하네스에서 쓸 수 있게 했다([9월 22일 일일](/jogan/daily/2026-09-22/#tech)).

**큰 하네스는 권한 확인과 기록 관리까지 맡는다.** Codex CLI는 모델이 파일을 고치거나 명령을 실행할 때 사용자에게 물을지, 묻지 않고 하게 둘지를 사용자가 고르게 한다([OpenAI](https://learn.chatgpt.com/docs/codex/cli)). Claude Code는 대화가 모델이 볼 수 있는 한도에 가까워지면 지난 기록을 자동으로 요약한다([Anthropic](https://code.claude.com/docs/en/costs)).

**몇 줄짜리 스크립트도 하네스다.** API로 모델을 부르고, 돌아온 도구 요청을 실행해 결과를 돌려주는 반복만 있으면 된다. 구글의 함수 호출 안내가 이런 모양의 예제를 싣고 있다([구글](https://ai.google.dev/gemini-api/docs/function-calling)). 하네스만 따로 오픈소스로 나오기도 한다([10월 3일 일일](/jogan/daily/2026-10-03/#tech)). 크든 작든 하는 일의 뼈대는 같다.

**[MCP](/jogan/terms/mcp/)는 하네스에 도구를 꽂는 규격이다.** MCP 공식 문서는 이를 AI 애플리케이션과 외부 시스템을 잇는 오픈소스 표준이라 소개하고, 전자기기의 USB-C 단자에 빗댄다. Claude, ChatGPT, VS Code, Cursor 등이 지원한다([MCP](https://modelcontextprotocol.io/docs/getting-started/intro)).

## 같은 모델, 다른 결과

2026년 9월 arXiv에 올라온 연구는 실행 반복은 그대로 두고 계획, 도구, 기록 관리 세 부품만 바꿔 가며 모델 네 개로 176가지 설정을 견줬다([arXiv, 2026](https://arxiv.org/abs/2609.20804), [9월 20일 일일](/jogan/daily/2026-09-20/#tech)).

- **기록 관리:** 모델이 볼 수 있는 양이 빠듯할수록 쓸모가 컸다. 효과는 대부분 기록이 넘쳐 작업이 실패하는 것을 막는 데서 나왔다.
- **계획:** 약한 모델에서는 정확도를 받쳐 줬고, 강한 모델에서는 정확도는 비슷한 채 비용을 줄였다.
- **도구:** 명령줄을 잘 다루는 모델은 명령줄 하나만 줘도 잘했고 비용이 크게 낮았다. 서툰 모델은 미리 만든 편집 도구의 도움을 받았다.

## 여러 에이전트를 엮는 것은 그 위의 일이다

**기본형은 모델 하나에 도구를 붙여 되풀이시키는 것이다.** OpenAI의 안내서는 모델 하나에 도구를 하나씩 늘려 가는 것만으로도 많은 일을 할 수 있다고 적었다([OpenAI](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)). NIST는 하위 에이전트 여럿을 조율하는 소프트웨어도 에이전트 시스템에 들어갈 수 있다고 본다([NIST](https://www.federalregister.gov/documents/2026/01/08/2026-00206/request-for-information-regarding-security-considerations-for-artificial-intelligence-agents)). 역할을 나눈 여러 에이전트를 파이프라인으로 엮는 것은 이 조율의 한 방식이다.

## 뉴스는 이렇게 읽는다

- **점수는 같은 하네스에서 쟀는지 본다.** 같은 모델도 하네스 설정에 따라 정확도와 비용이 달라진다.
- **비용도 하네스가 좌우한다.** 도구를 어떻게 주고 기록을 어떻게 줄이느냐에 따라 쓰는 [토큰](/jogan/terms/tokens/)이 달라진다.

## 출처

- [구글 — Gemini 함수 호출](https://ai.google.dev/gemini-api/docs/function-calling): 모델은 도구를 직접 실행하지 않는다
- [Anthropic — Claude Code 개요](https://code.claude.com/docs/en/overview): 코드 읽기·수정·명령 실행
- [Anthropic — Claude Code 비용 관리](https://code.claude.com/docs/en/costs): 기록 자동 요약
- [OpenAI — Codex CLI](https://learn.chatgpt.com/docs/codex/cli): 코드 수정·명령 실행, 권한 설정
- [MCP — 모델 컨텍스트 프로토콜 소개](https://modelcontextprotocol.io/docs/getting-started/intro): 도구를 잇는 오픈소스 표준
- [arXiv — 코딩 에이전트 하네스 설계 실증 연구(2026)](https://arxiv.org/abs/2609.20804): 세 부품, 176가지 설정 비교
- [OpenAI — 에이전트 만들기 안내서](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf): 단일 에이전트와 다중 에이전트
- [NIST — AI 에이전트 보안 의견 요청(2026년 1월)](https://www.federalregister.gov/documents/2026/01/08/2026-00206/request-for-information-regarding-security-considerations-for-artificial-intelligence-agents): 모델과 도구를 붙이는 소프트웨어
