// https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15StKqAQkCFAYD
// 연습용: TODO 구현 전에는 실행 시 예외가 발생합니다.
// 입력 파싱은 Main이 해줌. solution()만 구현.
// 섬 i는 (x[i], y[i]). 터널 길이 L -> 비용 e * L^2. 모든 섬을 잇는 최소 총비용을 반올림한 정수로 반환.
// 주의: 좌표 최대 1e6 -> dx*dx 는 int 오버플로우 (long 사용)
import java.util.*;

class Solution {
    record Node(int x, int y) {}
    public long solution(int[] x, int[] y, double e) {
        int n = x.length;
        boolean [] visited = new boolean[x.length];
        // cost, x, y
        PriorityQueue<long[]> pq = new PriorityQueue<>((a,b) -> Long.compare(a[0], b[0]));
        // cost, idx
        long total = 0;
        pq.add(new long[] {0,0});
        while (!pq.isEmpty()) {
            long[] curr = pq.poll();
            long cost = curr[0]; 
            int node = (int) curr[1];
            if (visited[node]) continue;
            visited[node] = true;
            total += cost;

            for (int next=0; next<n; next++) {
                if (visited[next]) continue;
                long dx = x[node] - x[next], dy = y[node] - y[next];
                pq.add(new long[] {dx * dx + dy * dy, next});
            }
        }
        return Math.round(total * e);
    }
}

public class Main {
    static int[] arr(int... a) { return a; }

    static void check(String name, long expected, long actual) {
        if (expected != actual) throw new AssertionError(name + ": expected=" + expected + ", actual=" + actual);
        System.out.println("PASS " + name + " -> " + actual);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // SWEA 공식 샘플 #1~#3
        check("sample1", 10000, sol.solution(arr(0, 0), arr(0, 100), 1.0));
        check("sample2", 180000, sol.solution(arr(0, 0, 400, 400), arr(0, 100, 0, 100), 1.0));
        check("sample3", 1125000, sol.solution(arr(0, 0, 400, 400, 1000, 2000), arr(0, 100, 0, 100, 600, 2000), 0.3));
        // 샘플 #4 (입력만 받음, 기대값은 직접 계산: Prim/Kruskal 두 방식 일치)
        check("sample4", 27365366, sol.solution(
                arr(567, 5, 45674, 24, 797, 29, 0, 0, 0),
                arr(345352, 5464, 145346, 54764, 5875, 0, 3453, 4545, 123), 0.0005));

        // 섬 1개: 터널 필요 없음
        check("N=1", 0, sol.solution(arr(5), arr(7), 1.0));
        // int 오버플로우 함정: L^2 = 2e12
        check("overflow", 2000000000000L, sol.solution(arr(0, 1000000), arr(0, 1000000), 1.0));

        // N=1000 최대 크기 (섬 1000개, 좌표 0~1e6, 고정 시드)
        int n = 1000;
        Random r = new Random(1);
        int[] bx = new int[n], by = new int[n];
        for (int i = 0; i < n; i++) {
            bx[i] = r.nextInt(1000001);
            by[i] = r.nextInt(1000001);
        }
        long t0 = System.currentTimeMillis();
        check("N=1000", 262967146L, sol.solution(bx, by, 0.0005));
        System.out.println("time " + (System.currentTimeMillis() - t0) + "ms");
    }
}
