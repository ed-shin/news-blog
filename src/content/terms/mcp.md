---
name: "MCP(모델 컨텍스트 프로토콜)"
title: "MCP란? AI 앱에 도구를 꽂는 공개 표준, 예시로 보기"
description: "AI 앱이 바깥의 도구와 자료를 같은 방식으로 연결하게 해 주는 공개 표준이다. 도구를 내놓는 서버를 한 번 만들면 MCP를 지원하는 여러 앱에서 쓸 수 있다. 연결 규격일 뿐, 모델을 어떻게 쓸지는 앱이 정한다."
category: "테크"
aliases: ["MCP", "모델 컨텍스트 프로토콜"]
related: ["harness", "ai-agent"]
pubDate: 2026-10-12
---

## 한 줄로 말하면

**AI 앱이 바깥의 도구와 자료를 같은 방식으로 연결하게 해 주는 공개 표준이다.** MCP 공식 문서는 이를 AI 애플리케이션과 외부 시스템을 잇는 오픈소스 표준으로 소개하고, 여러 전자기기를 같은 단자로 잇게 해 주는 USB-C에 빗댄다([MCP](https://modelcontextprotocol.io/docs/getting-started/intro)).

## 어떻게 움직이나

<figure class="chart diagram">
<svg viewBox="0 0 360 298" role="img" aria-label="MCP의 구조. 호스트인 AI 앱 안에 MCP 클라이언트가 셋 있다. 클라이언트는 서버마다 하나씩이고, 각 클라이언트는 MCP로 MCP 서버 하나와 이어진다. 서버는 파일, 데이터베이스, Sentry이고, 파일과 데이터베이스 서버는 내 컴퓨터에서, Sentry 서버는 인터넷 너머에서 돈다. 서버마다 도구·자료·프롬프트를 내놓는다.">
<defs><marker id="mcp-ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="ahead" d="M0 0 L10 5 L0 10 z"/></marker></defs>
<rect class="box host" x="8" y="8" width="344" height="124" rx="12"/>
<text class="lbl" x="22" y="32">호스트 · AI 앱</text>
<text class="sub" x="22" y="50">예: Claude · ChatGPT · VS Code · Cursor</text>
<rect class="box key" x="20" y="64" width="104" height="52" rx="6"/>
<text class="tag" x="72" y="86" text-anchor="middle">MCP 클라이언트</text>
<text class="sub" x="72" y="104" text-anchor="middle">서버마다 하나</text>
<line class="wire" x1="72" y1="118" x2="72" y2="190" marker-start="url(#mcp-ah)" marker-end="url(#mcp-ah)"/>
<text class="tag" x="79" y="159">MCP</text>
<rect class="box key" x="128" y="64" width="104" height="52" rx="6"/>
<text class="tag" x="180" y="86" text-anchor="middle">MCP 클라이언트</text>
<text class="sub" x="180" y="104" text-anchor="middle">서버마다 하나</text>
<line class="wire" x1="180" y1="118" x2="180" y2="190" marker-start="url(#mcp-ah)" marker-end="url(#mcp-ah)"/>
<text class="tag" x="187" y="159">MCP</text>
<rect class="box key" x="236" y="64" width="104" height="52" rx="6"/>
<text class="tag" x="288" y="86" text-anchor="middle">MCP 클라이언트</text>
<text class="sub" x="288" y="104" text-anchor="middle">서버마다 하나</text>
<line class="wire" x1="288" y1="118" x2="288" y2="190" marker-start="url(#mcp-ah)" marker-end="url(#mcp-ah)"/>
<text class="tag" x="295" y="159">MCP</text>
<rect class="box key" x="20" y="192" width="104" height="98" rx="6"/>
<text class="tag" x="72" y="212" text-anchor="middle">MCP 서버</text>
<text class="lbl" x="72" y="234" text-anchor="middle">파일</text>
<text class="sub" x="72" y="252" text-anchor="middle" style="font-size:11px">내 컴퓨터에서 돈다</text>
<text class="sub" x="72" y="276" text-anchor="middle" style="font-size:11px">도구·자료·프롬프트</text>
<rect class="box key" x="128" y="192" width="104" height="98" rx="6"/>
<text class="tag" x="180" y="212" text-anchor="middle">MCP 서버</text>
<text class="lbl" x="180" y="234" text-anchor="middle" style="font-size:13px">데이터베이스</text>
<text class="sub" x="180" y="252" text-anchor="middle" style="font-size:11px">내 컴퓨터에서 돈다</text>
<text class="sub" x="180" y="276" text-anchor="middle" style="font-size:11px">도구·자료·프롬프트</text>
<rect class="box key" x="236" y="192" width="104" height="98" rx="6"/>
<text class="tag" x="288" y="212" text-anchor="middle">MCP 서버</text>
<text class="lbl" x="288" y="234" text-anchor="middle" style="font-size:13px">Sentry</text>
<text class="sub" x="288" y="252" text-anchor="middle" style="font-size:11px">인터넷 너머에 있다</text>
<text class="sub" x="288" y="276" text-anchor="middle" style="font-size:11px">도구·자료·프롬프트</text>
</svg>
<figcaption>호스트(AI 앱)는 연결할 MCP 서버마다 MCP 클라이언트를 하나씩 만들고, 클라이언트는 짝이 된 서버와만 대화한다. 둘 다 MCP라는 같은 규격을 따르므로, 서버를 한 번 만들면 MCP를 지원하는 어느 앱에나 붙일 수 있다. 앱과 서버의 예는 MCP 공식 문서에 나온 것이다(<a href="https://modelcontextprotocol.io/docs/learn/architecture">MCP 구조</a>, <a href="https://modelcontextprotocol.io/docs/getting-started/intro">소개</a>).</figcaption>
</figure>

**서버가 내놓는 것은 세 가지다.** 실행할 수 있는 기능인 도구(파일 다루기, API 호출, 데이터베이스 조회), 맥락이 되는 자료(파일 내용, 데이터베이스 기록), 모델과 주고받을 대화 틀인 프롬프트다([MCP](https://modelcontextprotocol.io/docs/learn/architecture)).

## 날씨 묻기로 보면

MCP 문서에 실린 날씨 예시를 순서대로 풀면 이렇다([MCP](https://modelcontextprotocol.io/docs/learn/architecture)).

1. 호스트가 날씨 서버에 어떤 도구가 있는지 묻는다. 서버는 '현재 날씨' 도구와 필요한 입력(지역, 온도 단위)을 알려 준다.
2. 호스트는 연결된 서버들의 도구를 모아 모델에게 보여 준다.
3. 사용자가 "샌프란시스코 날씨 어때?"라고 묻자, 모델이 이 도구를 쓰겠다고 답한다.
4. 호스트가 그 요청을 날씨 서버로 보내고, 서버가 결과를 돌려준다.
5. 호스트가 결과를 모델에게 넣어 주고, 모델이 답을 쓴다.

**규격이 같아 한 번 만들면 여러 앱에서 쓴다.** 날씨 서버를 하나 만들면 MCP를 지원하는 어느 앱에나 붙일 수 있다. 공식 문서는 Claude, ChatGPT, VS Code, Cursor 등이 MCP를 지원한다고 적었다([MCP](https://modelcontextprotocol.io/docs/getting-started/intro)). OpenAI는 자사 API에서도 인터넷 너머의 MCP 서버로 모델을 새 자료와 기능에 연결할 수 있게 했다([OpenAI](https://developers.openai.com/api/docs/mcp/)).

## 누가 만들고 관리하나

**Anthropic이 2024년 11월 25일 처음 공개했다**([Anthropic](https://www.anthropic.com/news/model-context-protocol)). 지금은 리눅스 재단 계열의 LF Projects 아래 프로젝트로 운영된다. 기술 운영에 참여하는 자리는 회사가 아니라 개인에게 돌아가고, 특정 회사 몫으로 정해 둔 자리는 없다고 MCP 운영 규정은 적었다([MCP 운영 규정](https://modelcontextprotocol.io/community/governance)).

## 뉴스는 이렇게 읽는다

- **'MCP 지원'은 남이 만든 도구를 꽂을 수 있다는 뜻이다.** 2026년 10월 에이전트 실행 틀 Pi는 1.0을 내며 MCP를 기본 지원했고([10월 3일 일일](/jogan/daily/2026-10-03/#tech)), Cloudflare는 MCP 도구 운영자가 에이전트에게 사용료를 받게 하는 관문을 내놨다([10월 2일 일일](/jogan/daily/2026-10-02/#tech)).
- **꽂는 도구는 믿을 수 있는 것만 꽂는다.** OpenAI는 운영 주체를 알고 믿을 수 있지 않으면 사용자가 직접 고른 MCP 서버에 연결하지 말라고 권한다. 그런 서버는 OpenAI가 만들거나 검증한 것이 아니라고 적었다([OpenAI](https://developers.openai.com/api/docs/mcp/)). 도구가 돌려준 자료에 숨긴 지시로 에이전트를 휘두르는 공격도 있다([AI 에이전트](/jogan/terms/ai-agent/)).
- **연결 규격일 뿐이다.** 공식 문서는 MCP가 맥락을 주고받는 규약에만 집중하고, AI 앱이 모델을 어떻게 쓰거나 받은 맥락을 어떻게 다룰지는 정하지 않는다고 적었다([MCP](https://modelcontextprotocol.io/docs/learn/architecture)). 그 일은 하네스의 몫이다.

## 출처

- [MCP — 소개](https://modelcontextprotocol.io/docs/getting-started/intro): 오픈소스 표준, USB-C 비유, 지원하는 앱
- [MCP — 구조](https://modelcontextprotocol.io/docs/learn/architecture): 호스트·클라이언트·서버, 도구·자료·프롬프트, 날씨 예시, 규격의 범위
- [MCP — 운영 규정](https://modelcontextprotocol.io/community/governance): LF Projects 아래 운영, 개인 단위 참여
- [Anthropic — MCP 공개(2024년 11월 25일)](https://www.anthropic.com/news/model-context-protocol): 처음 공개
- [OpenAI — API의 MCP 지원](https://developers.openai.com/api/docs/mcp/): 원격 MCP 서버 연결과 신뢰 주의
