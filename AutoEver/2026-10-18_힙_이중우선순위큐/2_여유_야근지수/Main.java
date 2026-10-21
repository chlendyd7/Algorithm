// https://school.programmers.co.kr/learn/courses/30/lessons/12927
/**
 * 
 */
import java.util.*;

class Solution {
    public long solution(int n, int[] works) {
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b) -> Integer.compare(b,a));
        for (int work : works) {
            pq.add(work);
        }
        
        while (n!=0 && !pq.isEmpty()) {
            n--;
            int curr = pq.poll();
            if (curr == 1) continue;
            pq.add(curr-1);
        }

        long answer = 0;
        while (!pq.isEmpty()) {
            int curr = pq.poll();
            answer += curr*curr;
        }
        return answer;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution(4, new int[]{4,3,3}));
    }
}
