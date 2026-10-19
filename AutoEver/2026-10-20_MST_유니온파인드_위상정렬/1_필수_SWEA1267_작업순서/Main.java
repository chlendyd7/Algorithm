// https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18TrIqIwUCFAZN

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        for (int tc = 1; tc <= 10; tc++) {
            int V = sc.nextInt();
            int E = sc.nextInt();

            List<List<Integer>> graph = new ArrayList<>();
            for (int i = 0; i <= V; i++) graph.add(new ArrayList<>());
            int[] indegree = new int[V + 1];

            for (int i = 0; i < E; i++) {
                int a = sc.nextInt();   // a 먼저
                int b = sc.nextInt();   // b 나중
                graph.get(a).add(b);
                indegree[b]++;
            }

            Deque<Integer> q = new ArrayDeque<>();
            for (int i = 1; i <= V; i++) if (indegree[i] == 0) q.offer(i);

            sb.append("#").append(tc);
            while (!q.isEmpty()) {
                int cur = q.poll();
                sb.append(" ").append(cur);
                for (int next : graph.get(cur)) {
                    if (--indegree[next] == 0) q.offer(next);
                }
            }
            sb.append("\n");
        }
        System.out.print(sb);
    }
}
