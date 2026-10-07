---
name: "기대인플레이션과 실질금리"
title: "기대인플레이션(BEI)과 실질금리란? 금리 속 물가를 나누는 법"
description: "뉴스에 나오는 금리는 물가를 빼기 전의 명목금리다. 여기서 시장이 예상하는 물가(기대인플레이션)를 빼면 실질금리가 남는다. 미국에서는 물가연동국채로 이 둘을 나눠 볼 수 있다."
category: "물가"
aliases: ["기대인플레이션", "BEI", "실질금리"]
related: ["us-treasury-yields", "pce", "term-premium"]
pubDate: 2026-09-30
updatedDate: 2026-10-07
corrections:
  - date: 2026-10-07
    text: "두 국채 금리를 빼면 왜 물가 예상이 남는지와 '손익분기'라는 이름의 뜻, 순수한 예상만은 아니라는 점을 더했다. 이전 판은 빼면 남는다고만 적었다."
---

## 한 줄로 말하면

**금리 숫자 안에는 물가 몫이 들어 있다.** 세인트루이스 연은은 실질금리를 명목금리에서 기대인플레이션을 뺀 값으로 설명한다([세인트루이스 연은, 2023](https://www.stlouisfed.org/publications/page-one-economics/2023/01/03/adjusting-for-inflation)). 뒤집으면 뉴스에 나오는 금리(명목금리)는 실질금리에 기대인플레이션을 더한 값이다.

## 어떻게 계산하나

**미국에는 물가에 따라 원금이 불어나는 국채가 있다.** 물가연동국채(TIPS)다. 원금이 소비자물가(CPI)에 맞춰 오르내리고, 이자는 그 원금에 붙는다([재무부 TreasuryDirect](https://www.treasurydirect.gov/marketable-securities/tips/)). 물가만큼은 원금이 메워 주니, TIPS 금리는 물가를 빼고 남는 수익률, 곧 실질금리로 읽는다([세인트루이스 연은 FRED 블로그, 2021](https://fredblog.stlouisfed.org/2021/12/measuring-expected-inflation-with-breakevens/)).

**일반 국채 금리에서 같은 만기 TIPS 금리를 빼면 기대인플레이션이 남는다.** 앞으로 물가가 딱 그 차이만큼 오르면 어느 쪽을 사도 수익이 같아진다. 그래서 이 차이를 손익분기(breakeven) 인플레이션, 줄여 BEI라 부르고 시장이 예상하는 평균 물가로 읽는다([세인트루이스 연은 FRED 블로그, 2021](https://fredblog.stlouisfed.org/2021/12/measuring-expected-inflation-with-breakevens/)). 아래 예에서 10년물 5.01%와 TIPS 2.68%의 차이인 2.33%가 그 값이다.

## 왜 보나

**같은 금리라도 속이 다를 수 있다.** 2026년 9월 16일 연준이 금리를 올린 날 전후로 미국 [10년물](/jogan/terms/us-treasury-yields/)은 5.00%에서 5.01%로 거의 그대로였다. 그런데 안을 나누면 실질금리는 2.62%에서 2.68%로 오르고 기대인플레이션은 2.38%에서 2.33%로 내렸다. 시장이 연준의 인상을 물가를 잡겠다는 신호로 읽었다는 뜻이다([기획 글](/jogan/feature/rates-5-percent/)).

## 숫자는 이렇게 읽는다

- **기대인플레이션이 오르면** 시장이 앞으로 물가가 더 오를 것으로 본다는 뜻이다. 연준은 장기 기대인플레이션이 2%에 단단히 붙어 있어야 물가가 안정된다고 밝혀 왔다([연준 장기 목표 성명](https://www.federalreserve.gov/monetarypolicy/files/FOMC_LongerRunGoals.pdf)).
- **실질금리가 오르면** 물가를 빼고도 돈 빌리는 값이 비싸졌다는 뜻이다. 경기를 누르는 힘이 커진다.
- **순수한 예상만 담긴 숫자는 아니다.** 물가가 예상보다 더 오를 위험을 지는 대가가 들어 있어 실제 예상보다 높게 나오기 쉽다. 반대로 TIPS가 일반 국채보다 덜 거래되는 데 따른 대가는 이 값을 낮춘다([샌프란시스코 연은, 2011](https://www.frbsf.org/research-and-insights/publications/economic-letter/2011/06/tips-liquidity-breakeven-inflation-expectations/), [연준, 2004](https://www.federalreserve.gov/boarddocs/speeches/2004/20040415/default.htm)).
- **원인은 따로 봐야 한다.** 이 숫자는 시장이 무엇을 예상하는지만 보여 주고, 물가가 왜 그렇게 될지는 말해 주지 않는다([세인트루이스 연은 FRED 블로그, 2021](https://fredblog.stlouisfed.org/2021/12/measuring-expected-inflation-with-breakevens/)).

## 출처

- [재무부 TreasuryDirect — TIPS](https://www.treasurydirect.gov/marketable-securities/tips/): 원금이 CPI에 따라 오르내리는 국채
- [세인트루이스 연은 페이지 원 이코노믹스(2023)](https://www.stlouisfed.org/publications/page-one-economics/2023/01/03/adjusting-for-inflation): 실질금리 = 명목금리 − 기대인플레이션
- [세인트루이스 연은 FRED 블로그(2025)](https://fredblog.stlouisfed.org/2025/03/breakeven-inflation/): 기대인플레이션율(BEI)의 계산
- [세인트루이스 연은 FRED 블로그(2021)](https://fredblog.stlouisfed.org/2021/12/measuring-expected-inflation-with-breakevens/): TIPS 금리를 실질금리로 읽는 까닭, 손익분기라는 이름의 뜻, BEI가 알려 주지 않는 것
- [샌프란시스코 연은 이코노믹 레터(2011)](https://www.frbsf.org/research-and-insights/publications/economic-letter/2011/06/tips-liquidity-breakeven-inflation-expectations/): BEI에 섞인 물가 위험 대가와 유동성 대가
- [버냉키 연준 이사 연설(2004)](https://www.federalreserve.gov/boarddocs/speeches/2004/20040415/default.htm): 물가 위험 대가는 BEI를 높이고 유동성 대가는 낮춘다
