import java.util.*;

class Solution {
    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int test_case = 1; test_case <= T; test_case++) {
            // 여기에 알고리즘 코드 작성
            System.out.println("#" + test_case + " " + solve(sc));
        }
        
        sc.close();
    }

    static String solve(Scanner sc) {
        // 입력 받기
        int V = sc.nextInt();
        int E = sc.nextInt();
        int S1 = sc.nextInt();
        int S2 = sc.nextInt();
        // 알고리즘 로직
        
        List<Integer>[] graph = new ArrayList[V + 1];
        int[] parent = new int[V + 1];

        for (int i = 1; i <= V; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int i = 0; i < E; i++) {
            int s = sc.nextInt();
            int e = sc.nextInt();

            graph[s].add(e);
            parent[e] = s;
        }

        Set<Integer> ancestors = new HashSet<>();
        int current = S1;
        while (current != 0) {
            ancestors.add(current);
            current = parent[current];
        }

        int lca = 0;
        current = S2;
        while (current != 0) {
            if (ancestors.contains(current)) {
                lca = current;
                break;
            }
            current = parent[current];
        }

        int cnt = 0;
        Queue<Integer> queue = new ArrayDeque<>();
        queue.offer(lca);

        while (!queue.isEmpty()) {
            int now = queue.poll();
            cnt++;

            for (int child : graph[now]) {
                queue.add(child);
            }
        }

        return lca + " " + cnt;
    }
}
