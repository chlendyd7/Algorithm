// 자체 문제 (후기: "특정 지점을 거치는 경로 찾기", "최단경로 + 백트래킹/DP"를 바탕으로 만든 연습용)
// 연습용: TODO 구현 전에는 실행 시 예외가 발생합니다.
// 무방향 가중치 그래프. 노드 0..n-1, edges[i] = {a, b, w} (w > 0, 자기 자신/중복 간선 가능).
// s에서 출발해 via의 모든 노드를 (순서 상관없이) 지나서 t에 도착하는 최소 총 거리. 노드/간선 재방문 가능.
// 불가능하면 -1. via 원소는 서로 다르고 s, t와 같을 수 있다. via 길이 K <= 10.
// 제한: n <= 100,000, m <= 200,000, w <= 1,000,000,000 (합은 int를 넘는다 -> long)
// 힌트: 간선에 가중치가 있으면 BFS가 아니라 다익스트라.
//   방법 A: s, via[i]에서 각각 다익스트라 -> 핵심 노드 사이 최단거리 표 -> 순서 탐색(순열 또는 dp[방문 집합][마지막 노드])
//   방법 B: 상태 확장 다익스트라 dist[노드][via 통과 집합] (K가 작을 때)
import java.util.*;

class Solution {
    public long solution(int n, int[][] edges, int s, int t, int[] via) {
        // TODO
        throw new UnsupportedOperationException("TODO");
    }
}

public class Main {
    static int[][] E(int... a) {
        int[][] x = new int[a.length / 3][];
        for (int i = 0; i < x.length; i++) x[i] = new int[]{a[3 * i], a[3 * i + 1], a[3 * i + 2]};
        return x;
    }

    static void check(String name, long expected, long actual) {
        if (expected != actual) throw new AssertionError(name + ": expected=" + expected + ", actual=" + actual);
        System.out.println("PASS " + name + " -> " + actual);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[][] g1 = E(0,1,2, 1,2,3, 0,3,1, 3,2,1, 2,4,4);

        check("1 one via", 9, sol.solution(5, g1, 0, 4, new int[]{1}));            // 0-1-2-4
        check("2 no via", 6, sol.solution(5, g1, 0, 4, new int[]{}));            // 0-3-2-4
        check("3 via unreachable", -1, sol.solution(5, E(0,1,2, 1,2,3, 0,3,1, 3,2,1), 0, 3, new int[]{4}));
        int[][] chain = E(0,1,1000000000, 1,2,1000000000, 2,3,1000000000);
        check("4 int overflow", 3000000000L, sol.solution(4, chain, 0, 3, new int[]{}));
        check("5 via has s and t", 3000000000L, sol.solution(4, chain, 0, 3, new int[]{3, 0}));
        check("6 fewer edges but longer", 2, sol.solution(3, E(0,1,1, 1,2,1, 0,2,5), 0, 2, new int[]{}));
        check("7 revisit needed", 14, sol.solution(3, E(0,1,3, 0,2,4), 1, 1, new int[]{2}));   // 1-0-2-0-1
        check("8 any order", 5, sol.solution(6, E(0,1,1, 1,2,1, 2,3,1, 3,4,1, 4,5,1, 0,5,10), 0, 5, new int[]{3, 1, 4}));
        check("9 via equals t", 1, sol.solution(4, E(0,1,1, 2,3,1), 0, 1, new int[]{1}));

        // n=100,000, m=200,000, 경유지 5개 (고정 시드)
        int N = 100000;
        Random q = new Random(1);
        List<int[]> el = new ArrayList<>();
        for (int i = 0; i + 1 < N; i++) el.add(new int[]{i, i + 1, 1 + q.nextInt(1000000000)});
        for (int i = 0; i < 100001; i++) el.add(new int[]{q.nextInt(N), q.nextInt(N), 1 + q.nextInt(1000000000)});
        int[] via = new int[5];
        for (int i = 0; i < 5; i++) via[i] = q.nextInt(N);
        via = Arrays.stream(via).distinct().toArray();
        long t0 = System.currentTimeMillis();
        check("10 big graph", 19500716767L, sol.solution(N, el.toArray(new int[0][]), 0, N - 1, via));
        System.out.println("time " + (System.currentTimeMillis() - t0) + "ms");
    }
}
