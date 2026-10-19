# 2026-10-17

전체 플랜은 [../PLAN.md](../PLAN.md) 참고.

## 오늘 유형
- BFS/DFS (격자, 연결요소, 최단거리)
- 트리 부모배열로 조상 추적 (naive LCA — N 작아서 희소테이블 불필요)

## 문제 목록
BFS/DFS는 Python으로 이미 강한 부분 — 로직보다 Java 문법(큐 구현, 방문배열 등) 적응이 목적이라 가볍게.

**[필수]**
- 프로그래머스: 타겟 넘버 (Lv2, DFS)
- 프로그래머스: 게임 맵 최단거리 (Lv2, BFS)
- [프로그래머스: 미로 탈출](https://school.programmers.co.kr/learn/courses/30/lessons/159993) (Lv2, 레버 경유 BFS 2회) — 커버리지 점검(2026-10-19)으로 필수 추가. [연습 파일](./1_필수_미로탈출/Main.java)
- [프로그래머스: 무인도 여행](https://school.programmers.co.kr/learn/courses/30/lessons/154540) (Lv2, 격자 연결요소 크기) — 2차 점검(2026-10-19)으로 필수 추가. [연습 파일](./1_필수_무인도여행/Main.java)
- [LeetCode 994 Rotting Oranges](./1_필수_LC994_RottingOranges/README.md) (Medium, 멀티소스 BFS) — 2차 점검으로 필수 추가. 백준 접속 불가·프로그래머스에 대응 문제 미확인이라 LeetCode 선택. [연습 파일](./1_필수_LC994_RottingOranges/Main.java)

**[여유]**
- 프로그래머스: 아이템 줍기 (Lv2, BFS)
- [프로그래머스: 전력망을 둘로 나누기](https://school.programmers.co.kr/learn/courses/30/lessons/86971) (Lv2, 간선 제거 + 연결요소 크기, 트리) — 커버리지 점검으로 추가. [연습 파일](./2_여유_전력망을둘로나누기/Main.java)
- 프로그래머스: 네트워크 (Lv3, DFS/BFS)
- 프로그래머스: 단어 변환 (Lv3, BFS)
- SWEA 1226 미로1 (BFS, SWEA 사이트에서 번호로 검색)
- **SWEA 1248 공통조상** (D5, naive LCA — 부모배열로 루트까지 경로 추적 후 비교) — 오늘 유형에 적어둔 "트리 부모배열 조상추적"의 실제 커버 문제, 백준 다운돼서 대체로 찾음
