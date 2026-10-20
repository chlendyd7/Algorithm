// https://school.programmers.co.kr/learn/courses/30/lessons/42626
/*
peek()는 poll 하지 않고 하나만 보는 방법
poll(), offer(), size(), PriorityQueue()
PriorityQueue<.(Comparator.reverseOrder()); 최대 힙

*/
import java.util.*;

// 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
//  K 이상이 될 때까지 반복하여 섞습니다
// 섞어야 하는 최소 횟수


class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        for (int n : scoville) {
            minHeap.offer(n);
        }
        
        int cnt = 0;
        while (minHeap.peek() < K) {
            if (minHeap.size() < 2) {
                return -1;
            }
            minHeap.offer(minHeap.poll() + (minHeap.poll())*2);
            cnt += 1;
        }
        return cnt;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution());
    }
}
