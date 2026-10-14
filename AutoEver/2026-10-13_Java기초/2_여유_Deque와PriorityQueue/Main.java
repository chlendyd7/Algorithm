// Python: collections.deque, heapq 모듈 함수로 씀
// Java: ArrayDeque(스택/큐 둘 다 대용), PriorityQueue(힙) — 객체로 만들어서 메서드 호출
// 막히면 Answer.java 참고.

import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 예시: ArrayDeque를 큐처럼 — offer(1), offer(2) 하고 poll() 출력
        // 예상 출력: 1


        // 예시: ArrayDeque를 스택처럼 — push(1), push(2) 하고 pop() 출력
        // 예상 출력: 2


        // 예시: PriorityQueue 기본(최소힙) — offer(3), offer(1), offer(2) 하고 poll() 출력
        // 예상 출력: 1


        // 예시: PriorityQueue 최대힙 — new PriorityQueue<>(Collections.reverseOrder())로 만들고
        // offer(3), offer(1), offer(2) 하고 poll() 출력
        // 예상 출력: 3


        // 연습 1: int[] {5,2,8,1} 전부 PriorityQueue(최소힙)에 넣고 하나씩 poll()하면서 출력 (힙 정렬)
        // 예상 출력: 1 2 5 8


        // 연습 2: "level"을 한 글자씩 Deque에 addLast로 넣고
        // size()>1인 동안 pollFirst()/pollLast()로 양쪽에서 꺼내 비교해서 회문인지 확인
        // 예상 출력: level is palindrome: true

    }
}
