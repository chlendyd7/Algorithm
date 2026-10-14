# 2026-10-13 (Day 0) — Java 문법 자체 연습

전체 플랜은 [../PLAN.md](../PLAN.md) 참고.

알고리즘 로직은 Python으로 다 알고 있어서 문제없음. 여기는 **Java 언어 자체** 문법 적응 전용 — 10/14부터 시작하는 알고리즘 유형별 플랜 들어가기 전에 몸풀기.

각 폴더는 파일 2개 — **Answer.java**(설명 + 실행 가능한 정답, 참고용)와 **Main.java**(연습용, 코드는 비어있고 "뭘 작성해야 하는지" + "예상 출력"만 주석으로 있음). Main.java에 직접 타이핑해서 실행하고, 예상 출력이랑 맞는지 확인. 막히면 Answer.java 보고 확인.

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
