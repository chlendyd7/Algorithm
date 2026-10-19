# 최대 동시 프로세스 — start/end 힙 연습

- 출처: 지난 AutoEver 코테 첫 문제를 사용자 기억으로 재현한 **자체 문제**. 온라인 judge 없음.
- 같은 구조의 원문: [프로그래머스 호텔 대실](https://school.programmers.co.kr/learn/courses/30/lessons/155651) (gap=10). 이 문제를 풀면 별도 구현은 필요 없다.
- 우선순위: 필수. 연습 파일: [Main.java](./Main.java).

## 문제

작업 N개가 `[start, end]`로 주어진다(`start < end`, 정렬 안 됨). 한 프로세서는 `이전 end + gap <= 다음 start`일 때만 다른 작업을 이어받는다. 모든 작업에 필요한 **최소 프로세서 수**(= 최대 동시 실행 수)를 구한다.

| gap | 의미 |
|---|---|
| 0 | 끝나는 시각에 바로 다음 작업 시작 가능 |
| 1 | 끝난 다음 시각부터 재사용 (정수 시각에서 `end < start`) |
| 10 | 호텔 대실 (청소 10분) |

## 구현할 풀이 두 가지

1. `minProcessorsHeap`: start 정렬 → 종료 시각 최소 힙. 새 작업이 올 때 `heap.peek() + gap <= start`이면 `poll`(재사용), 아니면 그대로 `offer`. 답은 힙 크기의 최댓값(= 마지막 힙 크기).
2. `minProcessorsSweep`: 힙 없이. 종료 이벤트를 `end + gap`으로 옮기면 gap이 사라진다. 같은 시각이면 종료(-1)를 시작(+1)보다 먼저 처리한다.

두 풀이가 같은 결과를 내야 `check`를 통과한다.

## 확인할 조건

- 경계: 같은 시각의 종료와 시작은 `<=` 한 번이면 처리된다. 부등호가 하나라도 틀리면 gap=0/1 예제에서 걸린다.
- **오버플로**: `end + gap`이 int 범위를 넘을 수 있다. `long`으로 비교.
- 입력이 정렬돼 있다고 가정하지 않는다.
- Java: `PriorityQueue<Long>` 또는 `int[]` 비교자를 쓴다. 비교자에서 `a - b`는 오버플로 위험이 있으므로 `Integer.compare`/`Long.compare`.
- 목표 복잡도 O(N log N).

## 이 문제와 다른 문제

- 프로세서 번호까지 출력해야 하면 [CSES Room Allocation](../1_필수_CSES1164_RoomAllocation/README.md) (빈 프로세서 힙이 추가로 필요).
- 가장 많은 작업을 **고르는** 문제(NGV 강의실 배정)는 종료 시각 정렬 그리디다. 다른 문제다.
