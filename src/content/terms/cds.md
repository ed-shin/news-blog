---
name: "신용부도스와프(CDS)"
title: "CDS 뜻 — 신용부도스와프와 CDS 프리미엄 읽는 법"
description: "돈을 떼일 위험에 대비하는 보험 계약이다. 값은 보장받는 원금에 대한 1년 치 비율(bp)로 적는다. 실제 숫자로 계산해 보고, 프리미엄을 부도 확률로 그대로 읽으면 안 되는 까닭을 정리했다."
category: "시장"
aliases: ["신용부도스와프", "CDS", "신용파산스왑"]
related: ["us-treasury-yields"]
pubDate: 2026-10-20
updatedDate: 2026-10-23
corrections:
  - date: 2026-10-23
    text: "본문 문장을 이어 쓰고 출처를 문장 끝 괄호 대신 기관 이름에 걸었다. 사실과 숫자는 바꾸지 않았다."
---

## 한 줄로 말하면

**빌려준 돈을 떼일 위험을 다른 쪽에 넘기는 계약이다.** [한국은행](https://www.bok.or.kr/fileSrc/portal/d19eb6d6b1b84dd178076e17ca6a4d4e/1/202202151129019020.pdf) 『한국의 금융시장』에 따르면 보장을 사는 쪽이 파는 쪽에 정기적으로 돈을 내는데, 이것이 CDS 프리미엄이다. 돈을 빌린 회사나 나라에 신용사건이 생기면 손실을 보상받고, 사건이 없으면 프리미엄만 낸다. 신용사건은 파산, 빚을 제때 못 갚는 것, 지급정지 선언, 채무 재조정 등이다.

보상은 원금에서 부도 뒤 남은 가치를 뺀 만큼이다. [미 연준](https://www.federalreserve.gov/econres/feds/files/2022023pap.pdf) 논문의 예로, 1억 달러를 보장받았는데 부도 뒤 채권 가치가 1달러당 20센트라면 8,000만 달러를 받는다.

## 값은 어떻게 매기나

**보장받는 원금에 대한 1년 치 비율로, bp로 적는다.** 1bp는 0.01%다. [한국은행](https://www.bok.or.kr/fileSrc/portal/d19eb6d6b1b84dd178076e17ca6a4d4e/1/202202151129019020.pdf) 책자는 5년 만기 외평채(정부가 외화로 낸 채권) 1억 달러를 22.1bp로 보장하면 보장을 판 쪽이 매년 22.1만 달러를 받는다고 예를 든다.

- 1억 달러 × 0.221% = 22.1만 달러(한 해)

다만 프리미엄이 곧 해마다 내는 돈은 아니다. [미 연준](https://www.federalreserve.gov/econres/feds/files/2022023pap.pdf) 논문과 [BIS](https://www.bis.org/publications/the-big-bang-cds-market)에 따르면 표준 계약은 정해진 비율을 정기적으로 내고, 시장이 매긴 프리미엄과의 차이는 계약할 때 한 번에 정산한다. 그래서 "1,195bp면 100만 달러 보장에 한 해 11만 9,500달러"는 프리미엄을 1년 비용으로 바꿔 읽은 값이다.

## 왜 보나

**채권 시장이 그 회사나 나라의 부도 위험을 얼마로 보는지가 한 숫자로 나온다.** 한국의 CDS 프리미엄은 주로 외평채 5년물을 말하는데, [한국은행](https://www.bok.or.kr/fileSrc/portal/d19eb6d6b1b84dd178076e17ca6a4d4e/1/202202151129019020.pdf) 『한국의 금융시장』에 따르면 2008년 10월 692bp까지 올랐고 2021년 5월에는 19bp로 금융위기 뒤 가장 낮았다. 2026년 9월 평균은 [한국은행](https://www.bok.or.kr/portal/bbs/B0000502/view.do?nttId=11065634&menuNo=201265) 집계로 22bp였다.

회사도 같다. [더넥스트웹](https://thenextweb.com/news/huang-coreweave-backstop-stockholm)은 ICE 자료를 인용해 미국 AI 데이터센터 업체 코어위브의 5년 CDS가 2026년 10월 15일 장중 1,194.5bp로 기록상 가장 높았다고 전했다([10월 17일 일일](/jogan/daily/2026-10-17/#market)). S&P글로벌 마켓인텔리전스의 분석가는 [CNBC](https://www.cnbc.com/2026/10/15/coreweave-credit-default-swaps-hit-distress-levels-as-investors-sour-on-ai-debt.html)에 1,000bp 이상을 대개 신용 위기의 신호로 본다고 말했다.

## 숫자는 이렇게 읽는다

- **높을수록 시장이 부도 위험을 크게 본다.** [한국은행](https://www.bok.or.kr/fileSrc/portal/d19eb6d6b1b84dd178076e17ca6a4d4e/1/202202151129019020.pdf)은 프리미엄이 오르면 그 회사나 나라의 신용위험이 커진 것으로 평가된다는 뜻이라고 설명한다.
- **부도 확률이 아니다.** [연준](https://www.federalreserve.gov/econres/feds/files/2022023pap.pdf) 논문은 1년짜리 계약을 놓고 프리미엄 ≈ 부도 확률 × (1 − 회수율)이라는 단순한 식을 보인다. 22bp를 1년짜리 프리미엄으로 놓고 떼인 돈의 40%를 돌려받는다고 가정하면 0.22% ÷ 0.6 ≈ 0.37%다. 한국 5년물에서 앞으로 1년의 부도 확률을 직접 구한 값은 아니고, 시장 가격에서 거꾸로 푼 값이라 실제 확률과도 다르다. [BIS](https://www.bis.org/publ/qtrpdf/r_qt0512e.htm)는 프리미엄에 예상 손실 말고도 위험을 피하려는 웃돈이 들어 있다고 설명한다.
- **만기와 시점을 맞춰 견준다.** [미 연준](https://www.federalreserve.gov/econres/feds/files/2022023pap.pdf) 논문에 따르면 5년물이 가장 흔하다. 하루 안에서도 값이 크게 움직인다. 코어위브의 15일 장중 최고가는 [더넥스트웹](https://thenextweb.com/news/huang-coreweave-backstop-stockholm)이 전한 1,194.5bp였지만 같은 날 [CNBC](https://www.cnbc.com/2026/10/15/coreweave-credit-default-swaps-hit-distress-levels-as-investors-sour-on-ai-debt.html)가 마지막으로 전한 값은 약 1,038bp였다.
- **거래가 적으면 신호가 흐려진다.** [연준](https://www.federalreserve.gov/econres/feds/files/2022023pap.pdf) 논문은 미국 국채 CDS가 거래가 줄면서 덜 믿을 만한 지표가 됐다고 적었다.

## 출처

- [한국은행 『2021 한국의 금융시장』](https://www.bok.or.kr/fileSrc/portal/d19eb6d6b1b84dd178076e17ca6a4d4e/1/202202151129019020.pdf): 구조, 신용사건, 연율 표시, 외평채 예시와 역대 수준(389~402쪽)
- [한국은행 — 2026년 9월 이후 국제금융·외환시장 동향(2026년 10월 16일)](https://www.bok.or.kr/portal/bbs/B0000502/view.do?nttId=11065634&menuNo=201265): 외평채 CDS 월평균
- [미 연준 — Credit Default Swaps(FEDS 2022-023)](https://www.federalreserve.gov/econres/feds/files/2022023pap.pdf): 정의, 표준 쿠폰과 선급금, 부도 확률과의 관계, 유동성
- [BIS — CDS 시장의 '빅뱅'(2010)](https://www.bis.org/publications/the-big-bang-cds-market), [위험 회피와 CDS 위험 프리미엄(2005)](https://www.bis.org/publ/qtrpdf/r_qt0512e.htm)
