# 2026-10-20

전체 플랜은 [../PLAN.md](../PLAN.md) 참고.

## 오늘 유형
- MST (Kruskal/Prim, 필수 간선 선처리) — 저번 시험 출제 유형
- Union-Find
- 위상정렬

## 문제 목록
**[필수]** (MST, Union-Find, 위상정렬 하나씩 — MST/UF는 저번 시험 출제 유형)
- [프로그래머스: 섬 연결하기](https://school.programmers.co.kr/learn/courses/30/lessons/42861) (Lv3, MST — 크루스칼 정석 문제)
- [섬 연결하기 필수 연결 변형](./1_필수_섬연결하기_필수연결변형/README.md) — [연습 파일](./1_필수_섬연결하기_필수연결변형/Main.java). 이미 연결된 쌍 / 유료 필수 간선 / 트리 조건과 사이클을 구분한다.
- Codeforces 25D "Roads not only in Berland" (Union-Find) — https://codeforces.com/problemset/problem/25/D
- **SWEA 1267 작업순서** (위상정렬 정석 — 진입차수 0부터 큐 처리) — 2차 점검(2026-10-19)으로 [여유]에서 필수 승격. [연습 파일](./1_필수_SWEA1267_작업순서/Main.java). 3시간이 모자라면 필수 연결 변형보다 먼저 푼다(위상정렬은 이 문제 하나뿐이라 건너뛰면 유형이 통째로 빠진다).

**[여유]**
- SWEA 1251 하나로 (MST, 크루스칼/프림, SWEA 사이트에서 번호로 검색)
- AtCoder ABC120 D "Decayed Bridges" (Union-Find, 역순 처리) — https://atcoder.jp/contests/abc120/tasks/abc120_d

위상정렬: 4개 사이트에서 확실한 대표문제 특정 못함 → 재검색해서 찾음.
- 백준 복구되면: 2252 줄 세우기(입문) / 1766 문제집(힙+위상정렬) / 1005 ACM Craft(DP+위상정렬, 심화)
- 지금 당장: Codeforces 510C "Fox And Names", AtCoder ABC223 D (힙+위상정렬 콤보)

필수 연결 변형은 여유에서 필수로 승격했다. 자체 문제의 조건과 기대값은 해당 README 참고. 단순히 필수 쌍을 union하는 것은 "이미 연결된 경우"에만 비용 처리가 완성된다. 유료 필수 간선은 비용을 반드시 더하고, 결과를 트리로 제한하면 필수 간선의 사이클도 검사한다. 이번 NGV 공개 목록에는 이 조건과 직접 일치하는 문제를 찾지 못해 프로그래머스 섬 연결하기의 자체 변형을 사용한다.
