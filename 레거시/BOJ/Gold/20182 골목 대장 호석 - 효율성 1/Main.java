import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
    static int N, M, A, B;
    static long C;
    static List<Node>[] graph;
    static final long INF = Long.MAX_VALUE;

    static class Node implements Comparable<Node> {
        int to;
        long weight;

        public Node(int to, long weight) {
            this.to = to;
            this.weight = weight;
        }

        @Override
        public int compareTo(Node o) {
            return Long.compare(this.weight, o.weight);
        }

    }
    
    PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) -> Long.compare(o1.weight, o2.weight));

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        A = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());
        C = Long.parseLong(st.nextToken());

        graph = new ArrayList[N + 1];
        for (int i = 0; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            graph[u].add(new Node(v, w));
            graph[v].add(new Node(u, w));
        }

        int low = 1, high = 20;
        int answer = -1;

        while (low <= high) {
            int mid = (low + high) / 2;
            if (dijkstra(mid)) {
                answer = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        System.out.println(answer);
    }
    
    static boolean dijkstra(int limit) {
        long[] dist = new long[N + 1];
        Arrays.fill(dist, INF);
        dist[A] = 0;

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(A, 0));

        while (!pq.isEmpty()) {
            Node curr = pq.poll();

            if (dist[curr.to] < curr.weight)
                continue;
            if (curr.to == B)
                return dist[B] <= C;

            for (Node next : graph[curr.to]) {
                if (next.weight <= limit) {
                    long nextCost = curr.weight + next.weight;

                    if (nextCost <= C && nextCost < dist[next.to]) {
                        dist[next.to] = nextCost;
                        pq.add(new Node(next.to, nextCost));
                    }
                }
            }
        }
        return dist[B] <= C;
    }
}