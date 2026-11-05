---
title: "GitLab 취약점 CVE-2026-97229·110264 정리"
description: "GitLab이 10월 12일과 21일, 인증 없이도 서버에서 코드를 실행할 수 있다고 밝힌 결함 두 개(CVE-2026-97229·110264)를 고쳤다. 97229는 29일 미국 CISA의 실제 악용 목록에 올랐고, 11월 1일 집계로 110264에 취약한 서버는 1만 1,300대가 넘었다. 어느 판으로 올려야 하는지, 직접 빌드한 GitLab은 왜 Ruby까지 올려야 하는지 정리했다."
pubDate: 2026-11-05
tags: ["기획", "테크"]
searchTitle: "GitLab 취약점 CVE-2026-97229·110264 정리 — 영향 버전과 패치 방법 | 견문록"
period: { from: 2026-10-12, to: 2026-11-02 }
highlights:
  - { label: "심각도", value: "10.0 / 10", note: "두 결함 모두 GitLab 판정(CVSS 3.1)" }
  - { label: "고친 판", value: "19.5.1", note: "19.4.3·19.3.6 등, 10월 21일" }
  - { label: "아직 취약한 서버", value: "1만 1,300여 대", note: "110264 기준, Shadowserver 11월 1일" }
---

## 먼저 요점만

1. **GitLab은 10월에 인증 없이도 서버에서 코드를 실행할 수 있다고 밝힌 결함 두 개를 고쳤다.** 12일에 CVE-2026-97229를, 21일에 CVE-2026-110264를 고쳤고, 둘 다 취약점 심각도 점수(CVSS)를 10점 만점에 10.0으로 매겼다.
2. **회사 서버에 직접 설치한 GitLab이라면 21일에 나온 판으로 올려야 한다.** 19.5.1, 19.4.3, 19.3.6 등이고, 12일 판은 97229만 고쳤다. 공식 패키지가 아니라 따로 구한 Ruby로 돌린다면 Ruby도 올려야 하며, GitLab.com 이용자는 할 일이 없다.
3. **97229는 10월 29일 미국 CISA의 실제 악용 목록에 올랐다.** 11월 1일 Shadowserver 집계로 97229에 취약한 서버는 1,000대, 110264에 취약한 서버는 1만 1,300대가 넘었다.

## 영향 범위

**직접 설치해 운영하는 GitLab만 해당한다.** GitLab은 회사가 코드를 보관하고 빌드·시험·배포를 자동으로 돌리는(CI/CD) 개발 플랫폼으로, 회사 서버에 직접 설치해 쓰는 곳이 많다. [GitLab 공지](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-4-2-released/)에 따르면 GitLab.com은 이미 고친 판으로 돌고 있고, 전용 클라우드인 GitLab Dedicated는 공지를 내기 전에 내부 판으로 고쳤다.

영향을 받는 판은 두 결함이 다르다. 97229는 19.2~19.4 가운데 19.2.8, 19.3.5, 19.4.2보다 낮은 판이 대상이다. 반면 110264는 [GitLab 공지](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/)에 따르면 7.0 이후의 거의 모든 판대가 대상이고, 판대마다 21일에 나온 판보다 낮으면 취약하다.

인증이 정말 필요 없는지는 보는 쪽마다 다르다. GitLab은 97229로 특정 조건에서 인증 없이 코드를 실행할 수 있었다고 했지만, 97229를 재현한 보안업체 [Rapid7](https://www.rapid7.com/blog/post/etr-cve-2026-97229-critical-unauthenticated-remote-code-execution-in-gitlab/)은 공격하려면 저장소에 악성 CI/CD 설정을 심을 방법이 있어야 한다고 봤다. 다만 누구나 가입해 프로젝트를 만들 수 있는 서버라면 새로 가입한 계정으로 그 조건을 채울 수 있다고 덧붙였는데, 실제로 [Alpine Linux](https://alpinelinux.org/posts/gitlab-security-incident-cve-2026-97229/)의 GitLab을 노린 것도 새로 가입한 계정이었다.

## 올릴 판

**21일에 나온 판으로 올린다.** 12일 판(19.4.2·19.3.5·19.2.8)은 97229만 고쳤으므로, 110264까지 막으려면 21일 판이 필요하다.

| 쓰는 판대 | 두 결함을 고친 최소 판 |
|---|---|
| 19.5 | 19.5.1 |
| 19.4 | 19.4.3 |
| 19.3 | 19.3.6 |
| 19.2 | 19.2.9 |
| 19.1 | 19.1.9 |
| 19.0 | 19.0.10 |
| 18.11 | 18.11.13 |
| 7.0~18.10 | 같은 판대의 고친 판 없음 |

*출처: [GitLab 21일 공지](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/). 같은 판대에서 이 번호 이상이면 두 결함이 고쳐져 있다. 7.0~18.10도 110264의 영향을 받으므로 위 판 가운데 하나로 올려야 하고, 따로 구한 Ruby를 쓴다면 Ruby 판도 확인한다.*

판 번호는 끝자리까지 확인한다. [GitLab 공지](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-4-2-released/)에 따르면 19.3.4는 Ona 연동을 켠 경우 병합 요청 화면에 버그가 있어 19.3.5에서 고쳤는데, [Alpine](https://alpinelinux.org/posts/gitlab-security-incident-cve-2026-97229/)은 13일 19.3.5가 아닌 19.3.4로 올렸고 공격을 받을 때도 97229가 고쳐지지 않은 19.3.4였다.

업데이트하는 동안 서비스가 멈출 수 있다. [GitLab](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/)은 서버 한 대로 운영하면 데이터베이스 변경이 끝나야 GitLab이 다시 뜨므로 멈추고, 여러 대로 나눠 운영하면 무중단 절차로 멈추지 않고 올릴 수 있다고 안내했다.

### 직접 빌드했다면 Ruby도

**공식 패키지가 아닌 Ruby로 GitLab을 돌린다면 GitLab만 올려서는 막히지 않는다.** 두 결함은 GitLab이 쓰는 프로그래밍 언어 Ruby의 정규식 엔진에 있고, GitLab은 그 수정을 자기 공식 리눅스 패키지와 컨테이너 이미지에 넣은 Ruby에만 적용했다. 그래서 소스로 설치했거나 직접 만든 이미지로 돌린다면 [GitLab 공지](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/)대로 Ruby도 3.3.13, 3.4.12, 4.0.9 이상으로 올려야 하고, [Ruby](https://www.ruby-lang.org/en/news/2026/10/23/regexp-fixes-for-gitlab-cves/)는 이 판들을 10월 23일 냈다.

이 함정에 실제로 빠진 곳이 있다. [Alpine](https://alpinelinux.org/posts/gitlab-security-incident-cve-2026-97229/)은 22일 GitLab을 19.3.6으로 올렸지만 표준 Ruby를 쓰는 자체 이미지라 결함이 그대로 남았고, Ruby 3.3.13을 넣은 이미지는 27일에야 다시 냈다.

### 당장 올릴 수 없을 때

**GitLab 공지에는 업데이트 말고 다른 방법이 나와 있지 않다.** [Rapid7](https://www.rapid7.com/blog/post/etr-cve-2026-97229-critical-unauthenticated-remote-code-execution-in-gitlab/)은 올리기 전까지 공개 프로젝트에 익명 접근을 막고, 믿을 수 없는 사용자가 공개 프로젝트를 만들거나 쓰지 못하게 하면 노출을 줄일 수 있다고 했다. 다만 시연된 공격 경로만 막을 뿐 결함을 고치지는 못한다.

### 공격 흔적 점검

올린 뒤에는 공격 흔적을 살핀다. GitLab은 [97229 공지](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-4-2-released/)에 공격 시도를 찾는 탐지 규칙 여섯 개를, [110264 공지](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/)에 두 개를 올려 두었고, 두 공지 모두 정규식 엔진 때문에 작업 프로세스가 갑자기 죽는 것을 잡는 규칙을 담았다. [Alpine](https://alpinelinux.org/posts/gitlab-security-incident-cve-2026-97229/)도 공격받을 때 GitLab 작업 프로세스가 8번 죽었다.

## 실제 공격

**97229는 고친 판이 나온 지 17일 만에 실제 악용 목록에 올랐다.** 미국 사이버보안·인프라보안청([CISA](https://www.cisa.gov/news-events/alerts/2026/10/29/cisa-adds-two-known-exploited-vulnerabilities-catalog))은 10월 29일 실제 악용 증거를 근거로 97229를 '악용이 확인된 취약점' 목록(KEV)에 올렸다. 누가 공격했는지는 밝히지 않았다.

공격받은 곳이 경위를 직접 밝힌 사례도 있다. 리눅스 배포판 [Alpine Linux](https://alpinelinux.org/posts/gitlab-security-incident-cve-2026-97229/)에 따르면 20~21일 새로 가입한 계정이 조작한 CI 설정을 보내 97229를 노렸고, 공격은 성공 직전까지 갔다. Alpine은 성공한 증거는 찾지 못했지만 배제할 수 없어 서버를 처음부터 다시 만들었고, 배포 패키지와 21일 릴리스에는 변조 흔적이 없다고 밝혔다.

공격 도구도 공개돼 있다. [Rapid7](https://www.rapid7.com/blog/post/etr-cve-2026-97229-critical-unauthenticated-remote-code-execution-in-gitlab/)은 13일 공식 GitLab 이미지에서 코드 실행을 재현해 시연 코드를 올렸고, 침투 시험 도구 Metasploit에는 30일 [97229 공격 모듈](https://github.com/rapid7/metasploit-framework/pull/22017)이 들어갔다.

아직 고치지 않은 서버도 많다. 인터넷 서버를 살피는 비영리 단체 [Shadowserver](https://x.com/Shadowserver/status/2116995373264756914)는 11월 1일 매일 보는 GitLab 서버 약 3만 9,000대 가운데 97229에 취약한 서버가 1,000대, 110264에 취약한 서버가 1만 1,300대를 넘는다고 집계했다. 110264는 아직 KEV에 오르지 않았다.

**해설:** 고친 판이 나와도 서버가 취약한 채 남는 까닭을 Alpine의 경우가 보여 준다. 처음에는 번호가 하나 낮은 19.3.4로 올렸고, 다음에는 GitLab을 19.3.6으로 올렸지만 Ruby가 그대로여서 결함이 남았다. 직접 빌드해 운영한다면 GitLab 판 번호와 함께 Ruby 판도 확인해야 하는 이유다.

## 결함의 원리

**두 결함은 같은 곳에서 나왔지만 서로 다른 버그다.** 둘 다 GitLab이 정규식(문자열의 패턴을 찾는 식)을 컴파일할 때 숫자가 표현할 수 있는 범위를 넘어 엉뚱한 값이 되는 정수 오버플로이고, [GitLab](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/)에 따르면 같은 연구자 joaxcar가 버그 신고 포상 프로그램(HackerOne)으로 보고했다. [Ruby](https://www.ruby-lang.org/en/news/2026/10/23/regexp-fixes-for-gitlab-cves/)에 따르면 97229는 컴파일된 패턴의 크기를 세는 값이 넘치는 버그로, 9월 23일 GitLab 19.4.1이 고친 CVE-2026-93577과 뿌리가 같다. 110264는 반복이 많은 패턴에서 내부 번호가 넘치는 다른 버그다.

두 결함이 드러나는 길도 다르다. [GitLab 공지](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-4-2-released/)에 따르면 97229는 CI/CD 설정에 넣은 조작한 정규식으로 서버에서 코드를 실행할 수 있었고, 110264는 [조작한 정규식을 컴파일하는 순간](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/) 일어난다.

같은 위험은 Ruby로 만든 다른 앱에도 있다. [Ruby](https://www.ruby-lang.org/en/news/2026/10/23/regexp-fixes-for-gitlab-cves/)에 따르면 이 버그는 공격자가 정한 문자열로 정규식을 만드는 앱에서 드러나고, 개발자가 직접 쓴 정규식만 쓰는 앱은 영향이 없다. Ruby의 정규식 시간 제한(`Regexp.timeout`)으로는 막히지 않는다.

## 국내 대응

**한국인터넷진흥원(KISA)은 보호나라에 두 차례 업데이트를 권고했다.** [10월 14일 권고](https://www.boho.or.kr/kr/bbs/view.do?searchCnd=&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=1&categoryCode=&nttId=72215)는 97229를, [22일 권고](https://www.boho.or.kr/kr/bbs/view.do?searchCnd=&bbsId=B0000133&searchWrd=&menuNo=205020&pageIndex=1&categoryCode=&nttId=72232)는 110264를 비롯한 결함 다섯 개를 다뤘다.

## 다음에 볼 것

- **110264가 실제 악용 목록에 오르는지.**
  지금까지 KEV에 오른 것은 97229뿐이고, 110264는 11월 4일 목록에 없다. 그런데 취약한 서버는 110264 쪽이 열 배가 넘는다.
  CISA KEV 목록과 GitLab 공지의 갱신을 보면 된다.
  목록에 오르면 110264도 실제 공격에 쓰이고 있다는 뜻이고, 오르지 않으면 지금까지 실제 악용이 확인된 것은 97229뿐이다.
- **취약한 서버 수가 줄어드는지.**
  11월 1일 Shadowserver 집계로 97229에 취약한 서버는 1,000대, 110264에 취약한 서버는 1만 1,300대가 넘었다.
  Shadowserver의 다음 집계를 보면 된다.
  숫자가 크게 줄면 업데이트가 퍼진 것이고, 그대로면 공격받을 수 있는 서버가 그만큼 남아 있다는 뜻이다.
