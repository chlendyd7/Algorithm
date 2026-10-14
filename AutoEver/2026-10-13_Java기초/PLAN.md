# 2026-10-13 (Day 0) — Java 문법 자체 연습

전체 플랜은 [../PLAN.md](../PLAN.md) 참고.

알고리즘 로직은 Python으로 다 알고 있어서 문제없음. 여기는 **Java 언어 자체** 문법 적응 전용 — 10/14부터 시작하는 알고리즘 유형별 플랜 들어가기 전에 몸풀기.

각 폴더 Main.java는 전부 **설명 + 실행 가능한 정답 코드**로 채워져 있음 (빈 TODO 아님) — 읽고 직접 실행해보면서 왜 이렇게 쓰는지 이해하는 게 목적. 다 이해했으면 변형해서 다시 짜보는 식으로 복습.

## 오늘 유형
**[필수]** — 코테 전체에서 매일 쓰게 될 기본기
- 변수와 타입 (오버플로, int/long 캐스팅)
- 배열과 ArrayList (`[]` vs `List<>`, 깊은 복사)
- 문자열 (equals vs ==, StringBuilder, split/substring)
- 해시맵과 해시셋 (HashMap/HashSet 기본 메서드, entrySet 순회)
- 클래스와 메서드 (프로그래머스 `class Solution { solution() }` 패턴)
- 입출력 (BufferedReader/StringTokenizer — SWEA/CF/AtCoder용, 프로그래머스는 해당없음)
- 형변환과 기본 메서드 (char↔int 변환, Math 메서드, Integer 비교 함정) — 점검 중 빠진 걸 발견해서 추가함

**[여유]** — 나오면 쓰지만 급하면 나중에
- Comparator와 정렬 (10/15에서 본격적으로 또 다룸)
- Deque와 PriorityQueue (10/18에서 본격적으로 또 다룸)
- 제네릭 기초 (그래프 인접리스트 만들 때 필요)
- 람다와 스트림 (몰라도 for문으로 다 풀림, 제일 뒤로 미뤄도 됨)
