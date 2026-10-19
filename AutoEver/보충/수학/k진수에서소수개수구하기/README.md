# k진수에서 소수 개수 구하기

- 원문: [프로그래머스 Lv2](https://school.programmers.co.kr/learn/courses/30/lessons/92335)
- 우선순위: 수학 보충 중 **우선**. 진법 변환 + 소수 판별 + long 오버플로를 한 문제로 확인한다.
- 연습 파일: [Main.java](./Main.java)

## 연습 목표

진법 변환은 `Integer.toString(n, k)` 또는 직접 나눗셈으로 한다. 직접 변환을 한 번은 써 본다. 문자열을 `split("0")`으로 자르고 소수를 센다. 30분 안에 끝낸다.

## 확인할 조건

- 조각 값이 `int` 범위를 넘을 수 있다 (n≤1,000,000, k=3이면 최대 13자리). `Long.parseLong` 사용. `Integer.parseInt`는 런타임 예외.
- 소수 판별 루프에서 `i * i`도 long으로 계산. int로 쓰면 오버플로.
- `split("0")`은 연속된 0에서 빈 문자열을 만든다. 빈 문자열은 건너뛴다. `"1".equals("")` 같은 비교 말고 `isEmpty()`.
- 0과 1은 소수 아님.
- k=10이면 n 자체를 0 기준으로 자른다.

예제 4개는 Main.java에 있다. 기대값은 기준 풀이로 확인했다.
