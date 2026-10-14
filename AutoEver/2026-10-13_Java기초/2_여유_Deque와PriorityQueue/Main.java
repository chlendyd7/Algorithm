// Python: collections.deque, heapq 모듈 함수로 씀
// Java: ArrayDeque(스택/큐 둘 다 대용), PriorityQueue(힙) — 객체로 만들어서 메서드 호출
// (10/18 힙 날에 깊게 쓸 거라 여기선 기본 사용법만)

import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 예시: ArrayDeque를 큐처럼 쓰기 (offer=넣기, poll=꺼내기)
        Deque<Integer> queue = new ArrayDeque<>();
        queue.offer(1);
        queue.offer(2);
        System.out.println(queue.poll()); // 1 (먼저 넣은 게 먼저 나옴, FIFO)

        // 예시: ArrayDeque를 스택처럼 쓰기 (push/pop) — java.util.Stack은 레거시라 비추천
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(1);
        stack.push(2);
        System.out.println(stack.pop()); // 2 (나중에 넣은 게 먼저 나옴, LIFO)

        // 예시: PriorityQueue — 기본은 최소힙 (작은 값이 먼저 나옴)
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        minHeap.offer(3);
        minHeap.offer(1);
        minHeap.offer(2);
        System.out.println(minHeap.poll()); // 1

        // 예시: 최대힙 — Comparator.reverseOrder()로 뒤집기 (Python은 heapq에 음수 넣어서 흉내냄)
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        maxHeap.offer(3);
        maxHeap.offer(1);
        maxHeap.offer(2);
        System.out.println(maxHeap.poll()); // 3

        // TODO 1: int[] {5, 2, 8, 1} 을 전부 PriorityQueue(최소힙)에 넣고
        // 하나씩 poll()하면서 오름차순으로 출력해보기 (힙 정렬 느낌).


        // TODO 2: 회문(팰린드롬) 체크할 때 자주 쓰는 패턴 — Deque 양쪽에서 꺼내서 비교.
        // "level" 문자를 한 글자씩 Deque에 다 넣고, pollFirst()/pollLast()로 양쪽에서
        // 하나씩 꺼내 비교하면서 회문인지 확인해보기.

    }
}
