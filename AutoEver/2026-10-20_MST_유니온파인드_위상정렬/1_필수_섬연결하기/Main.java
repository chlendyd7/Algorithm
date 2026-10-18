// https://school.programmers.co.kr/learn/courses/30/lessons/42861

import java.util.*;

class Solution {
    record Node (int target, int weight) {};
    
    public int solution(int n, int[][] costs) {
        List<List<Node>> graph = new ArrayList<>();
        for (int i=0; i<n; i++) graph.add(new ArrayList<>());
        for (int i=0; i<costs.length; i++) {
            int s = costs[i][0];
            int e = costs[i][1];
            int w = costs[i][2];
            
            graph.get(s).add(new Node(e, w));
            graph.get(e).add(new Node(s, w));
        }
        
        boolean[] visited = new boolean[n];
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) -> a[0] - b[0]);
        pq.add(new int[] {0,0});
        
        int totalCost = 0;
        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int weight = curr[0], node = curr[1];
            if (visited[node]) continue;
            visited[node] = true;
            totalCost += weight;
            
            for(Node edge: graph.get(node)) {
                int next = edge.target(), w = edge.weight();
                if (!visited[next]) pq.offer(new int[] {w, next});
            }
        }
        
        return totalCost;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution());
    }
}
