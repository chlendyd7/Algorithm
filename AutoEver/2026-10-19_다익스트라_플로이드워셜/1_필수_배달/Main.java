// https://school.programmers.co.kr/learn/courses/30/lessons/12978

import java.util.*;
import java.util.*;

class Solution {
    record Node(int target, int weight) {}
    
    public int solution(int N, int[][] road, int K) {
        List<List<Node>> graph = new ArrayList<>();
        for (int i=0; i<=N; i++) graph.add(new ArrayList<>());
        for (int[] r: road) {
            int u = r[0];
            int v = r[1];
            int w = r[2];
            graph.get(u).add(new Node(v,w));
            graph.get(v).add(new Node(u,w));
        }
        
        
        int start = 1;
        int[] dist = new int[N+1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[start] = 0;
        
        PriorityQueue<int[]> pq = new PriorityQueue<>((x,y) -> x[1] - y[1]);
        pq.offer(new int[] {start, 0});
        
        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int node = curr[0];
            int d = curr[1];
            
            if (d>dist[node]) continue;
            
            for (Node next: graph.get(node)) {
                int nextNode = next.target();
                int weight = next.weight();
                
                if (dist[node] + weight < dist[nextNode]) {
                    dist[nextNode] = dist[node] + weight;
                    pq.offer(new int[]{nextNode, dist[nextNode]});
                }
            }
        }
        
        int answer = 0;
        for (int i=1; i<= N; i++) {
            if (dist[i]<=K) {
                answer++;
            }
        }
        return answer;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution());
    }
}
