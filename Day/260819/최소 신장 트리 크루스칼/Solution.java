import java.util.*;

class Solution {
    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int test_case = 1; test_case <= T; test_case++) {
            System.out.println("#" + test_case + " " + solve(sc));
        }
        
        sc.close();
    }

    static int solve(Scanner sc) {
        int V = sc.nextInt();
        int E = sc.nextInt();

        List<List<Edge>> graph = new ArrayList<>();
        for (int i = 0; i <= V; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < E; i++) {
            int s = sc.nextInt();
            int e = sc.nextInt();
            int w = sc.nextInt();

            graph.get(s).add(new Edge(w, e));
            graph.get(e).add(new Edge(w, s));
        }

        PriorityQueue<Edge> pq = new PriorityQueue<>();
        boolean[] visited = new boolean[V + 1];

        pq.offer(new Edge(0, 0));
        long totalWeight = 0;
        int cnt = 0;

        while (!pq.isEmpty()){
            Edge current = pq.poll();
            int weight = current.weight;
            int node = current.node;

            if (visited[node]) {
                continue;
            }

            if (cnt >= V+1) {
                break;
            }

            totalWeight += weight;
            cnt ++;
            visited[node] = true;

            for (Edge next : graph.get(node)) {
                pq.offer(next);
            }

        }

        return (int)totalWeight;
    }
    

    static class Edge implements Comparable<Edge> {
        int weight;
        int node;

        Edge(int weight, int node) {
            this.weight = weight;
            this.node = node;
        }

        @Override
        public int compareTo(Edge other) {
            return this.weight - other.weight;
        }
    }
}
