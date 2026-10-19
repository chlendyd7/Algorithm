# 2026-10-18

전체 플랜은 [../PLAN.md](../PLAN.md) 참고.

## 오늘 유형
- 힙/우선순위큐 기본
- 이중 우선순위 큐 (Lazy Deletion) — 힙 2개를 쓰는 한 가지 패턴
- 자원 배정: 사용 중인 자원은 종료 시간순, 빈 자원은 번호순으로 관리

## 문제 목록
**[필수]**
- [더 맵게](https://school.programmers.co.kr/learn/courses/30/lessons/42626) (Lv2, 힙 기본 — 익숙하면 짧게 복습)
- [이중우선순위큐](https://school.programmers.co.kr/learn/courses/30/lessons/42628) (Lv3, 최소/최대 힙과 삭제 상태 동기화)
- [CSES Room Allocation](https://cses.fi/problemset/task/1164/) (자원 배정) — [연습 파일](./1_필수_CSES1164_RoomAllocation/Main.java), [설명](./1_필수_CSES1164_RoomAllocation/README.md). 원문은 임의의 유효한 방 번호를 허용한다. 연습에서는 "빈 방 중 최소 번호 우선" 조건을 추가해 두 힙을 모두 사용한다.

- [최대 동시 프로세스](./1_필수_최대동시프로세스/README.md) (지난 시험 1번 재현, 자체 문제) — start/end 정렬 + 종료 시각 힙, 스위핑 두 가지로 구현. gap=10이면 [프로그래머스 호텔 대실](https://school.programmers.co.kr/learn/courses/30/lessons/155651)과 동일. [연습 파일](./1_필수_최대동시프로세스/Main.java)
- [디스크 컨트롤러](https://school.programmers.co.kr/learn/courses/30/lessons/42627) (Lv3, 힙 — 요청 시각 정렬 + 작업 시간 힙으로 대기 작업 관리) — **필수로 승격**(2026-10-19). 폴더 이름도 `1_필수_디스크컨트롤러`로 변경. [연습 파일](./1_필수_디스크컨트롤러/Main.java).

지난 시험의 "힙 2번"만으로 이중우선순위큐라고 단정하지 않는다. 필수 패턴을 각각 연습할 것: 최소/최대 동기화(이중우선순위큐), 자원 배정 두 힙(CSES), 시간 흐름에 따른 대기열(디스크 컨트롤러). 백준 12764는 이번 확인 시 문제 대신 서비스 안내 페이지가 나와 채점 가능한 CSES를 선택했다.

**[여유]**
- 프로그래머스: 야근 지수 (Lv3, 힙)

**[선택]** (필수를 다 끝내고도 시간이 남을 때만)
- [LeetCode 1882 Process Tasks Using Servers](https://leetcode.com/problems/process-tasks-using-servers/) (Medium, 빈 서버 힙 + 사용 중 서버 힙) — [설명·예제](./3_선택_ProcessTasksUsingServers/README.md), [연습 파일](./3_선택_ProcessTasksUsingServers/Main.java). 10/23 모의풀이의 후보 문제이기도 하므로, 모의풀이 전에 풀었다면 같은 유형의 다른 미풀이 문제로 교체한다.
