# Python -> Java 변환 연습 (itertools, deque.rotate)

- 근거: 후기 "사용한 알고리즘은 DP, deque rotate, 백트래킹(product와 combinations)" (본문 기준, 회사/회차는 적혀 있지 않았다).
- 우선순위: 필수. 5분짜리 손풀기. 연습 파일: [Main.java](./Main.java) (틀 + 테스트)
- Java에는 `itertools`가 없어서 직접 재귀로 써야 한다. 이 파일이 막힘없이 나오면 N과 M 계열은 끝.

## 핵심

- `product`(중복순열): 매번 `1..n` 전부 시도, `depth == m`이면 저장.
- `combinations`(조합): `start`를 다음 호출에 `i + 1`로 넘겨서 중복/순서를 막는다.
- `permutations`(순열): `visited[]`로 이미 쓴 수를 거른다.
- 저장할 때 `pick.clone()` (같은 배열을 계속 바꾸므로 복사 필수. 불량 사용자 때 본 "복사 안 하면 set이 깨진다"와 같은 이유).
- `rotate`: `dq.addFirst(dq.pollLast())`를 k번(`k %= n`), 음수면 `addLast(pollFirst())`.
- 백준은 종료돼 문제 링크 대신 원본 번호만 적었다. LeetCode 77(Combinations), 46(Permutations)이 같은 유형이다.
