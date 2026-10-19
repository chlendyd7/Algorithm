// https://school.programmers.co.kr/learn/courses/30/lessons/155651?language=java

import java.util.*;

import java.util.*;

class Solution {
    record Node(int start, int end) {};
    record roomUse(int start, int end, int roomNum){};
    
    public int solution(String[][] book_time) {
        int n = book_time.length;
        int need = 0;
        
        PriorityQueue<Node> remainQ = new PriorityQueue<>((a,b) -> Integer.compare(a.start, b.start));
        PriorityQueue<Node> useQ = new PriorityQueue<>((a,b) -> Integer.compare(a.end, b.end));
        
        for (int i=0; i<n; i++) {
            String[] curr = book_time[i];
            remainQ.offer(new Node(toMin(curr[0]), toMin(curr[1])));
        }
        
        int roomNum = 1;
        boolean[] room = new boolean[n+1];
        
        // 가장 최근 종료되는거 꺼내서 비교
        // 가능한 케이스는?
        int answer = 0;
        while (!remainQ.isEmpty()) {
            // 비교해야하는 케이스
            while (!useQ.isEmpty() && remainQ.peek().start >= useQ.peek().end + 10) {
                useQ.poll();
            }
            useQ.offer(remainQ.poll());
            answer = Math.max(useQ.size(), answer);
        }
        
        return answer;
    }
    
    int toMin(String s) {                  // "15:30" → 930
        return Integer.parseInt(s.substring(0, 2)) * 60 + Integer.parseInt(s.substring(3));
    }
}