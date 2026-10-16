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

지난 시험의 "힙 2번"만으로 이중우선순위큐라고 단정하지 않는다. 두 필수 패턴을 각각 연습할 것. 백준 12764는 이번 확인 시 문제 대신 서비스 안내 페이지가 나와 채점 가능한 CSES를 선택했다.

**[여유]**
- 프로그래머스: 디스크 컨트롤러 (Lv3, 힙)
- 프로그래머스: 야근 지수 (Lv3, 힙)
