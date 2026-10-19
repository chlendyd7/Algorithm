# 2026-10-22

전체 플랜은 [../PLAN.md](../PLAN.md) 참고.

## 오늘 유형
- DP (1차원, 배낭, LIS)
- 그리디 (정렬 기준)

## 문제 목록
**[필수]**
- 프로그래머스: 정수 삼각형 (Lv2, DP 기본)
- 프로그래머스: 체육복 (Lv1, 그리디 기본)
- [NGV 징검다리](https://exam.hyundai-ngv.com/practice/6293) (Lv3, LIS — N≤3000이라 O(N²) DP부터) — [연습 파일](./1_필수_NGV_징검다리/Main.java).
- [NGV 강의실 배정](https://exam.hyundai-ngv.com/practice/6291) (Lv3, 종료 시간 정렬+구간 그리디) — [연습 파일](./1_필수_NGV_강의실배정/Main.java).

정수 삼각형 → **등굣길** → 징검다리 → 강의실 배정 순으로 우선 진행. 체육복이 익숙하면 복습만 한다. 배낭까지 전부 당일에 몰지 말고 시간 남을 때 아래 Knapsack 1을 진행.

- **등굣길은 정수 삼각형 다음 우선 보완** (2026-10-19): 필수 4개와 별도로 정수 삼각형 바로 뒤에 푼다. 둘 다 2차원 격자/삼각형 DP라 이어서 풀면 점화식 설계가 연결된다. 웅덩이(막힌 칸) 처리, `1,000,000,007` 나머지 연산, 웅덩이 좌표가 `[열, 행]` 순서라는 점이 포인트. 폴더는 `2_여유_등굣길` 그대로 두었다(필수 승격은 아님, 순서만 앞당김).
- **Java 배낭(Knapsack) 경험이 없다면 기존 [Knapsack 1](https://atcoder.jp/contests/dp/tasks/dp_d)을 진행** — [연습 파일](./2_여유_EDPC_D_Knapsack1/Main.java). 새 배낭 문제를 찾지 말고 이 파일 하나로 `dp[w]` 점화식을 Java로 처음부터 구현해 본다. 확인 포인트: 가치 합이 `int` 범위를 넘을 수 있어 `long`, 1차원 배열로 줄일 때 무게 루프를 **뒤에서 앞으로** 돌리기. 배낭을 이미 Java로 풀어 본 적이 있다면 건너뛰고 LCS/Frog 1 쪽으로 넘어간다.

**[여유]**
- 프로그래머스: 도둑질 (Lv4, 원형 배열에서 인접 원소를 함께 고르지 않는 DP — 배낭 문제가 아님). 기존 폴더 이름은 유지하되 학습 우선순위는 여유로 낮춤.
- 프로그래머스: N으로 표현 (Lv3, DP)
- 프로그래머스: 등굣길 (Lv3, DP)
- 프로그래머스: 조이스틱 (Lv2, 그리디)
- AtCoder Educational DP Contest A "Frog 1" — https://atcoder.jp/contests/dp/tasks/dp_a
- AtCoder Educational DP Contest D "Knapsack 1" — https://atcoder.jp/contests/dp/tasks/dp_d
- AtCoder Educational DP Contest F "LCS" — https://atcoder.jp/contests/dp/tasks/dp_f
