---
name: "VIX(변동성지수)"
title: "VIX란? 변동성지수 뜻과 숫자 읽는 법"
description: "S&P 500 옵션 가격으로 계산한, 앞으로 30일 동안 미국 주가가 얼마나 출렁일지에 대한 시장의 예상이다. 1년 기준 %로 적어, 20이면 한 달에 위아래 약 5.8%의 움직임이 옵션 가격에 들어 있다는 뜻이다."
category: "시장"
aliases: ["VIX", "변동성지수"]
related: ["sox", "circuit-breaker"]
pubDate: 2026-11-26
---

## 한 줄로 말하면

**S&P 500 옵션 가격에 담긴, 앞으로 30일 동안 미국 주가가 얼마나 출렁일지에 대한 시장의 예상이다.** 미국 옵션거래소 [Cboe](https://cdn.cboe.com/api/global/us_indices/governance/Volatility_Index_Methodology_Cboe_Volatility_Index.pdf)가 1993년 처음 내놓았고, 2003년 지금처럼 S&P 500 옵션으로 계산하는 방식으로 바꿨다. 흔히 '공포 지표'로 불린다.

## 어떻게 계산하나

**만기가 30일 앞뒤인 S&P 500 옵션 두 묶음의 가격을 모아 30일 변동성을 구한다.** 옵션은 정해진 값(행사가)에 지수를 사거나(콜) 팔(풋) 권리이고, 앞으로 지수가 크게 출렁일 것으로 보일수록 비싸진다. 그래서 옵션 가격에는 앞으로의 변동성에 대한 시장의 예상이 들어 있다([Cboe 방법론](https://cdn.cboe.com/api/global/us_indices/governance/Volatility_Index_Methodology_Cboe_Volatility_Index.pdf)). [Cboe 수학 방법론](https://cdn.cboe.com/api/global/us_indices/governance/Cboe_Volatility_Index_Mathematics_Methodology.pdf)은 만기가 30일 이하인 근월물과 그 뒤 만기인 차근월물을 고르게 하고, [Cboe의 2023년 해설](https://www.cboe.com/insights/posts/what-the-vix-and-vix-1-d-indices-attempt-to-measure-and-how-they-differ)은 이 옵션들의 만기가 23~37일 사이에 있다고 설명한다.

묶음마다 쓰는 옵션은 지금 행사하면 이익이 나지 않는 외가격 옵션이다. 먼저 옵션 가격으로 지수의 선도 가격을 구하고, 그 바로 아래 행사가를 기준 행사가로 삼는다. 기준보다 행사가가 낮은 쪽은 풋, 높은 쪽은 콜을 행사가마다 하나씩 담는데, 매수나 매도 호가가 0인 옵션은 빼고 그런 행사가가 두 번 이어지면 그 바깥은 더 보지 않는다([Cboe 수학 방법론](https://cdn.cboe.com/api/global/us_indices/governance/Cboe_Volatility_Index_Mathematics_Methodology.pdf)). 가격은 매수·매도 호가의 중간값이다.

이어 옵션마다 가격에 행사가 간격과 금리 몫을 곱하고 행사가의 제곱으로 나눠 모두 더한 뒤, 선도 가격과 기준 행사가의 차이만큼 덜어 내 그 만기의 분산(변동성의 제곱, 1년 기준)을 구한다. 두 만기의 분산에 각각 남은 기간을 곱해 30일에 맞게 가중평균하고, 다시 1년 기준으로 바꿔 제곱근에 100을 곱한다.

[Cboe 방법론](https://cdn.cboe.com/api/global/us_indices/governance/Volatility_Index_Methodology_Cboe_Volatility_Index.pdf) 부록은 가상 호가로 이 과정을 한 번 계산해 보인다.

1. 만기가 24일 남은 근월물과 31일 남은 차근월물을 고른다.
2. 두 묶음의 분산(1년 기준)은 0.019234와 0.019424다. 제곱근으로 바꾸면 변동성 약 13.87%와 13.94%다.
3. 두 분산에 남은 기간을 곱해 30일에 맞게 섞는다. 30일은 31일 쪽에 가까워 차근월물에 약 83%, 근월물에 약 17%의 비중이 간다.
4. 섞은 값을 다시 1년 기준으로 바꿔 제곱근을 구하면 0.13928이고, 100을 곱한 13.93이 VIX다.

## 왜 보나

**주가가 급히 빠지는 날 함께 뛰어, 시장이 느끼는 불안의 크기를 숫자 하나로 보여 준다.** [Cboe의 2022년 해설](https://www.cboe.com/insights/posts/inside-volatility-trading-breaking-down-the-vix-index-and-its-correlation-to-the-s-p-500-index)은 S&P 500이 내릴 때 VIX가 대체로 오른다고 쓴다. 주가가 내리면 하락에 대비하려는 수요가 늘어 VIX 계산에 들어가는 풋 가격이 오르기 때문이다([Cboe, 2023](https://www.cboe.com/insights/posts/what-the-vix-and-vix-1-d-indices-attempt-to-measure-and-how-they-differ)). 예를 들어 [파이낸셜뉴스](https://www.fnnews.com/news/202611060625255827)가 전한 2026년 11월 5일(현지)에는 S&P 500이 4.36% 내리고 VIX가 69.48% 뛴 28.15에 닿았다([11월 6일 일일](/jogan/daily/2026-11-06/#market)).

다만 늘 반대로 움직이지는 않는다. [Cboe](https://www.cboe.com/insights/posts/what-the-vix-and-vix-1-d-indices-attempt-to-measure-and-how-they-differ)는 둘이 같은 방향으로 움직이는 날이 약 20%라고 밝힌다. 같은 글은 VIX가 시장 심리 전체를 재는 지표가 아니고, 다음 날 주가나 다른 자산의 움직임을 알려 주지도 않는다고 쓴다.

## 숫자는 이렇게 읽는다

- **30일 예상을 1년 기준 %로 늘려 적은 숫자다.** 오를지 내릴지는 담지 않고 폭만 담는다. 그래서 한 달로 읽으려면 12가 아니라 √12(약 3.46)로 나눈다. 변동성은 기간의 제곱근에 비례해 커지기 때문이다.
- **표준편차 하나로 읽는다.** [Cboe 해설](https://www.cboe.com/insights/posts/inside-volatility-trading-breaking-down-the-vix-index-and-its-correlation-to-the-s-p-500-index)은 정규분포를 가정해, VIX 28이면 S&P 500이 한 달 동안 위아래 약 8.1% 안에서 움직일 확률을 68%로 보는 셈이라고 설명한다. VIX 20이면 약 5.8%다. 정규분포는 가정이라 실제 확률을 약속하지는 않는다.
- **보통은 10대 후반이다.** [FRED](https://fred.stlouisfed.org/series/VIXCLS)에 실린 1990년 1월 2일부터 2026년 11월 24일까지의 종가를 보면 중앙값은 17.57이고, 가장 낮은 종가는 2017년 11월 3일의 9.14다. 가장 높은 종가는 코로나19 충격 때인 2020년 3월 16일의 82.69, 그다음이 금융위기 때인 2008년 11월 20일의 80.86이다.
- **등락률은 VIX 숫자 자체의 변화다.** "VIX 69.48% 급등"은 VIX가 16대에서 28대로 올랐다는 뜻이다.

## 출처

- [Cboe — VIX 방법론(버전 6.0, 2026년 2월 26일 개정)](https://cdn.cboe.com/api/global/us_indices/governance/Volatility_Index_Methodology_Cboe_Volatility_Index.pdf): 30일 기대 변동성이라는 정의, 1993년 도입과 2003년 개편, 외가격 풋·콜과 매수 호가 0 규칙, 호가 중간값, 가상 계산 예시(VIX 13.93), '공포 지표'라는 별명
- [Cboe — 변동성지수 수학 방법론(버전 5.0)](https://cdn.cboe.com/api/global/us_indices/governance/Cboe_Volatility_Index_Mathematics_Methodology.pdf): 근월물 선택, 행사가 제곱에 반비례하는 비중, 두 만기를 30일로 맞추는 가중평균 식
- [Cboe 해설(2023)](https://www.cboe.com/insights/posts/what-the-vix-and-vix-1-d-indices-attempt-to-measure-and-how-they-differ): 만기 23~37일, 방향 없는 1년 기준 표준편차, 하락 때 풋 수요, 같은 방향으로 움직이는 날 약 20%
- [Cboe 해설(2022)](https://www.cboe.com/insights/posts/inside-volatility-trading-breaking-down-the-vix-index-and-its-correlation-to-the-s-p-500-index): S&P 500과 반대로 움직이는 경향, 68% 확률 읽기, 한 달 환산에 √12
- [FRED — VIXCLS](https://fred.stlouisfed.org/series/VIXCLS): Cboe 자료를 실은 일별 종가(2026년 11월 26일 내려받은 자료)
