// https://school.programmers.co.kr/learn/courses/30/lessons/468373
//
import java.util.*;

class Solution {
    List<Map<Integer, List<Integer>>> graph;
    int n;
    int k;
    int answer;
    
    public int solution(int n, int infection, int[][] edges, int k) {
        this.n = n;
        this.k = k;
        this.answer = 0;
        graph = new ArrayList<>();
        
        for (int i=0; i<n+1; i++) graph.add(new HashMap<>());
        for (int[] edge: edges) {
            int a = edge[0];
            int b = edge[1];
            int value = edge[2];
            
            graph.get(a).computeIfAbsent(value, key -> new ArrayList<>()).add(b);
            graph.get(b).computeIfAbsent(value, key -> new ArrayList<>()).add(a);
        }
        boolean [] infected = new boolean[n+1];
        infected[infection] = true;
        dfs(0, infected);
        
        return answer;
    }

    public void dfs(int count, boolean[] infected) {
        int infectedCount = 0;
        for (int node = 1; node<=n; node++) {
            if(infected[node]) {
                infectedCount++;
            }
        }
        answer = Math.max(answer, infectedCount);
        if (count == k || infectedCount == n) {
            return;
        }
        
        for (int type = 1; type<=3; type++) {
            boolean[] next = infected.clone();
            spread(type, next);
            dfs(count+1, next);
        }
    }
    public void spread(int type, boolean[]infected) {
        Queue<Integer> queue = new ArrayDeque<>();
        
        for (int node=1; node<=n; node++) {
            if(infected[node]) {
                queue.offer(node);
            }
        }
        while (!queue.isEmpty()) {
            int current = queue.poll();
            List<Integer> neighbors = graph.get(current).get(type);
            if (neighbors == null) continue;
            
            for (int next: neighbors) {
                if(infected[next]) continue;
                infected[next] = true;
                queue.offer(next);
            }
        }
    }
}
