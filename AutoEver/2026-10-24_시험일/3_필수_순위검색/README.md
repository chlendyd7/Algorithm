# 순위 검색

- 원문: [프로그래머스 Lv2](https://school.programmers.co.kr/learn/courses/30/lessons/72412) (연습 틀은 10/21 폴더의 것과 같음)
- 우선순위: 필수. 2025 하반기 후기의 "이분탐색 + 구현(입력 파싱에서 막힘)" 유형 대비. 연습 파일: [Main.java](./Main.java)

## 연습 목표

- `info`, `query` 문자열을 `split`으로 파싱하는 것부터 직접 쓴다. `" and "`가 섞인 query 파싱이 포인트.
- 지원자 1명당 조건 조합 16개(각 항목 값 또는 "-")를 키로 `HashMap<String, List<Integer>>`에 점수를 저장 -> 정렬 -> query마다 lower bound.
- info 5만, query 10만이라 query마다 info 전체를 훑으면 시간 초과.
