// https://school.programmers.co.kr/learn/courses/30/lessons/42627
import java.util.*;
import java.util.*;
//[[0, 3], [1, 9], [3, 5]]	8
// 가장 우선순위가 높은 작업을 대기 큐에서 꺼내서 작업
// 작업 소요시간이 짧은 것, 작업의 요청 시간이 빠른 것, 작업의 번호가 작은 것 우선순위
// [작업이 요청되는 시점, 작업의 소요시간]

class Solution {
    //startTime, workingTime, idx
    record Node (int sTime, int wTime, int i) {}
    
    public int solution(int[][] jobs) {
        int n = jobs.length;
        int[] answerList = new int[n];
        PriorityQueue<Node> reqQ = new PriorityQueue<>((x,y) -> Integer.compare(x.sTime, y.sTime));
        for (int i=0; i<n; i++) reqQ.offer(new Node(jobs[i][0], jobs[i][1], i));
        
        PriorityQueue<Node> pq = new PriorityQueue<>((x,y) -> {
            if (x.wTime() != y.wTime()) return Integer.compare(x.wTime(), y.wTime());
            if (x.sTime() != y.sTime()) return Integer.compare(x.sTime(), y.sTime());
            return Integer.compare(x.i(), y.i());
        });
        
        
        int time = 0, total = 0;
        while (!reqQ.isEmpty() || !pq.isEmpty()) {
            while (!reqQ.isEmpty() && reqQ.peek().sTime() <= time) pq.offer(reqQ.poll());
            
            if (pq.isEmpty()) {
                time = reqQ.peek().sTime();
                continue;
            }
            
            Node cur = pq.poll();
            time += cur.wTime();
            total += time - cur.sTime();
        }
        
        
        return total/n;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution());
    }
}
