---
name: "하네스(에이전트 하네스)"
title: "AI 하네스란? 뜻과 작동 방식"
description: "AI 모델이 '이걸 하겠다'고 낸 도구 요청을 실제로 실행하고, 그 결과를 다시 모델에게 돌려주는 소프트웨어다. 같은 모델도 어떤 하네스에서 돌리느냐에 따라 결과와 비용이 달라진다."
category: "테크"
aliases: ["하네스"]
related: ["ai-agent", "mcp", "tokens"]
pubDate: 2026-10-12
updatedDate: 2026-10-23
corrections:
  - date: 2026-10-14
    text: "연구 소개에서 '명령줄 하나만 준' 설정이라고 썼으나, 파일·검색 전용 도구를 빼고 명령줄을 남긴 설정이었고 계획·기록용 보조 도구는 그대로였다. '여러 에이전트를 엮는 것은 하네스 그 위의 일'이라고 단정한 것도, 같은 연구가 여러 에이전트를 조율하는 하네스를 소개하고 있어 바로잡았다. 두 코딩 도구를 같은 항목으로 나란히 적고, MCP를 Anthropic이 처음 공개했다는 사실과 순환 그림, 연구의 숫자를 더했다."
  - date: 2026-10-23
    text: "제목을 「AI 하네스란? 모델에게 손발을 달아 주는 틀, 예시로 보기」에서 「AI 하네스란? 뜻과 작동 방식」으로 바꾸고, 소제목 「버그 하나 고치기로 보면」을 「어떻게 움직이나」로, 「같은 모델, 다른 결과」를 「부품별 성공률과 비용」으로, 「하나를 돌리기도, 여럿을 조율하기도 한다」를 「단일 에이전트와 다중 에이전트」로 바꿨다. 본문 문장을 이어 쓰고 출처를 문장 끝 괄호 대신 기관·회사 이름에 걸었다. 사실과 숫자는 바꾸지 않았다."
---

## 한 줄로 말하면

**AI 모델이 '이걸 하겠다'고 낸 도구 요청을 실제로 실행하고, 그 결과를 다시 모델에게 돌려주는 소프트웨어다.** 모델은 글자만 내놓을 뿐, 직접 파일을 열거나 명령을 실행하지 못한다. [구글](https://ai.google.dev/gemini-api/docs/function-calling)에 따르면 모델은 도구를 써 달라는 요청을 정해진 형식으로 낼 뿐이고, 실행해 결과를 돌려주는 일은 모델을 부르는 프로그램이 맡는다. 이 일을 맡는 틀이 하네스이고, 모델과 하네스를 합친 것이 [AI 에이전트](/jogan/terms/ai-agent/)다.

## 어떻게 움직이나

**모델이 할 일을 고르면 하네스가 실행하고 결과를 돌려준다.** 사용자가 "이 버그를 고쳐 줘"라고 맡기면, 하네스는 모델에게 도구 목록을 보내는 데서 시작해 테스트가 통과하거나 정해 둔 횟수에 닿을 때까지 요청과 실행을 되풀이한다.

<figure class="chart diagram">
<svg viewBox="0 0 360 460" role="img" aria-label="모델과 하네스의 반복 구조. 모델이 도구 이름과 입력값을 담은 요청을 내면 하네스가 도구를 실행한다. 하네스가 결과를 모델에게 돌려주면 모델이 다음 행동을 판단한다. 끝날 때까지 이 순환을 되풀이한다.">
<defs><marker id="harness-ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="ahead" d="M0 0 L10 5 L0 10 z"/></marker></defs>
<rect class="box key" x="84" y="16" width="248" height="84" rx="8"/>
<text class="lbl" x="208" y="44" text-anchor="middle">모델</text>
<text class="sub" x="208" y="66" text-anchor="middle">결과를 보고 다음 행동을 고른다</text>
<text class="sub" x="208" y="86" text-anchor="middle">끝났으면 답변을 낸다</text>
<line class="wire" x1="208" y1="100" x2="208" y2="194" marker-end="url(#harness-ah)"/>
<text class="tag" x="220" y="140">도구 요청</text>
<text class="sub" x="220" y="160">이름 + 입력값</text>
<rect class="box host" x="76" y="194" width="276" height="234" rx="12"/>
<text class="lbl" x="92" y="218">하네스 · 실행을 맡는 틀</text>
<rect class="box" x="96" y="238" width="236" height="60" rx="6"/>
<text class="lbl" x="214" y="262" text-anchor="middle">요청받은 도구를 실행한다</text>
<text class="sub" x="214" y="284" text-anchor="middle">파일 읽기 · 수정 · 명령 실행</text>
<line class="wire" x1="214" y1="298" x2="214" y2="350" marker-end="url(#harness-ah)"/>
<rect class="box" x="96" y="350" width="236" height="58" rx="6"/>
<text class="lbl" x="214" y="374" text-anchor="middle">실행 결과를 받는다</text>
<text class="sub" x="214" y="396" text-anchor="middle">파일 내용 · 수정 결과 · 오류</text>
<path class="wire" d="M96 379 H24 V58 H84" marker-end="url(#harness-ah)"/>
<text class="tag" x="34" y="126">결과를</text>
<text class="tag" x="34" y="146">돌려준다</text>
<text class="sub" x="180" y="451" text-anchor="middle">끝날 때까지 되풀이한다</text>
</svg>
<figcaption>모델은 쓸 도구를 고르고, 하네스는 실행과 결과 전달을 맡는다. 결과를 받은 모델이 다음 요청이나 답을 낸다.</figcaption>
</figure>

1. 하네스가 과제와 함께 쓸 수 있는 도구(파일 읽기·고치기, 명령 실행) 목록을 모델에게 보낸다.
2. 모델이 파일 읽기 도구로 a.py를 열어 달라고 요청하면, 하네스가 실제로 파일을 읽어 내용을 돌려준다.
3. 모델이 12번째 줄을 이렇게 고치라고 요청하면 하네스가 파일을 고친다.
4. 모델이 테스트를 돌려 달라고 하면 하네스가 돌리고, 실패 메시지를 돌려준다.
5. 2~4를 되풀이한다. 기록이 모델이 한 번에 볼 수 있는 양을 넘으려 하면 하네스가 오래된 것을 덜거나 요약한다.
6. 테스트가 통과하거나 정해 둔 횟수에 닿으면 멈춘다.

요리사가 모델이라면 하네스는 주방이다. 같은 요리사라도 어떤 칼과 오븐을 갖췄는지(도구), 레시피를 먼저 짜는지(계획), 좁은 작업대에서 다 쓴 재료를 어떻게 치우는지(기록 관리)에 따라 속도와 재료비가 달라진다.

## 하네스는 어디에 있나

**AI 코딩 도구가 대표적인 하네스다.** [Anthropic](https://code.claude.com/docs/en/overview)의 Claude Code와 [OpenAI](https://learn.chatgpt.com/docs/codex/cli)의 Codex CLI(터미널에서 쓰는 코딩 도구)는 모두 코드를 읽고, 파일을 고치고, 명령을 실행한다. Cursor 같은 편집기도 여러 회사의 모델을 받아 쓰는 하네스다([9월 22일 일일](/jogan/daily/2026-09-22/#tech)).

이런 큰 하네스는 권한과 기록까지 맡는다. [Anthropic](https://code.claude.com/docs/en/permissions)과 [OpenAI](https://learn.chatgpt.com/docs/codex/cli) 문서에 따르면 두 도구 모두 파일을 고치거나 명령을 실행하기 전에 물을지를 사용자가 정한다. 대화가 길어지면 둘 다 지난 기록을 요약하는데, [Claude Code](https://code.claude.com/docs/en/costs)는 한도에 가까워지면 자동으로, [Codex CLI](https://learn.chatgpt.com/docs/developer-commands?surface=cli)는 `/compact` 명령으로 한다.

작게는 몇 줄짜리 스크립트도 하네스다. [구글](https://ai.google.dev/gemini-api/docs/function-calling)의 예제처럼 API(프로그램이 모델을 부르는 창구)로 모델을 부르고, 돌아온 도구 요청을 실행해 결과를 돌려주면 된다. 하네스만 따로 오픈소스로 나오기도 한다([10월 3일 일일](/jogan/daily/2026-10-03/#tech)).

**[MCP](/jogan/terms/mcp/)는 하네스에 도구를 꽂는 공개 규격이다.** [Anthropic](https://www.anthropic.com/news/model-context-protocol)이 2024년 11월 25일 처음 공개했다.

## 부품별 성공률과 비용

**같은 모델도 하네스 부품을 바꾸면 성공률과 비용이 달라진다.** 2026년 9월 논문 공개 저장소 [arXiv](https://arxiv.org/html/2609.20804v1)에 올라온 연구는 계획, 도구, 기록 관리 세 부품을 바꿔 가며 모델 네 개로 176가지 설정을 견줬고, 실제 GitHub 이슈 500건과 터미널 과제 89건에서 과제 성공률과 과제당 비용을 쟀다([9월 20일 일일](/jogan/daily/2026-09-20/#tech)).

- **기록 관리:** 모델이 볼 수 있는 양이 빠듯할수록 쓸모가 컸다. 버그 과제에서 기록 관리를 켠 쪽의 성공률이 3만 2,000토큰일 때 평균 35.7%p, 12만 8,000토큰일 때 2.7%p 높았다.
- **계획:** 약한 모델에서는 성공률을 받쳐 줬고, 강한 모델에서는 성공률은 비슷한 채 비용을 줄였다.
- **도구:** 파일·검색 전용 도구를 빼고 명령줄만 남긴 설정(계획·기록용 보조 도구는 유지)에서, 명령줄을 잘 다루는 모델은 비용을 줄였다. 서툰 모델은 전용 도구의 도움을 받았다.

## 단일 에이전트와 다중 에이전트

**기본형은 모델 하나에 도구를 붙여 되풀이시키는 것이고, 여러 에이전트를 조율하는 하네스도 있다.** [OpenAI](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) 안내서는 모델 하나에 도구를 늘려 가는 것만으로도 많은 일을 할 수 있다고 적었다. 한편 앞의 [arXiv](https://arxiv.org/html/2609.20804v1) 연구는 작업 순서도와 역할별 하위 에이전트를 더한 하네스도 소개하고, [NIST](https://www.federalregister.gov/documents/2026/01/08/2026-00206/request-for-information-regarding-security-considerations-for-artificial-intelligence-agents)도 하위 에이전트를 조율하는 소프트웨어를 에이전트 시스템에 넣는다. 역할을 나눈 에이전트들을 파이프라인으로 엮는 것도 그 한 방식이다.

## 뉴스는 이렇게 읽는다

- **점수는 같은 하네스에서 쟀는지 본다.** 같은 모델도 하네스 설정에 따라 성공률과 비용이 달라진다.
- **비용도 하네스가 좌우한다.** 도구를 어떻게 주고 기록을 어떻게 줄이느냐에 따라 쓰는 [토큰](/jogan/terms/tokens/)이 달라진다.

## 출처

- [구글 — Gemini 함수 호출](https://ai.google.dev/gemini-api/docs/function-calling): 도구 요청과 실행
- [Anthropic — Claude Code 개요](https://code.claude.com/docs/en/overview), [권한](https://code.claude.com/docs/en/permissions), [비용 관리](https://code.claude.com/docs/en/costs): 기능, 승인, 기록 요약
- [OpenAI — Codex CLI](https://learn.chatgpt.com/docs/codex/cli), [명령](https://learn.chatgpt.com/docs/developer-commands?surface=cli): 기능, 승인, 기록 요약
- [Anthropic — MCP 공개(2024년 11월 25일)](https://www.anthropic.com/news/model-context-protocol)
- [arXiv — 코딩 에이전트 하네스 설계 실증 연구(2026)](https://arxiv.org/html/2609.20804v1): 실험 조건과 결과, 여러 에이전트 조율
- [OpenAI — 에이전트 만들기 안내서](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf): 단일·다중 에이전트
- [NIST — AI 에이전트 보안 의견 요청(2026년 1월)](https://www.federalregister.gov/documents/2026/01/08/2026-00206/request-for-information-regarding-security-considerations-for-artificial-intelligence-agents): 하위 에이전트 조율
