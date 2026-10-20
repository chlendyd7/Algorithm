import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        int tc = 10;

        for (int t=1; t<=tc; t++) {
            int V = sc.nextInt();
            int E = sc.nextInt();

            List<List<Integer>>graph = new ArrayList<>();
            for (int i=0; i<=V; i++) graph.add(new ArrayList<>());
            int[] indegree = new int[V+1];

            for (int i=0; i<E; i++) {
                int a = sc.nextInt();
                int b = sc.nextInt();
                graph.get(a).add(b);
                indegree[b] ++;
            }

            Deque<Integer> q = new ArrayDeque<>();
            for (int i=1; i<=V; i++) if (indegree[i] == 0) q.add(i);

            sb.append("#").append(t);
            while (!q.isEmpty()) {
                int curr = q.poll();
                sb.append(" ").append(curr);
                for (int node: graph.get(curr)) {
                    --indegree[node];
                    if (indegree[node] == 0) {
                        q.add(node);
                    }
                }
            }
            sb.append("\n");
        }
        System.out.print(sb);
    }
}
