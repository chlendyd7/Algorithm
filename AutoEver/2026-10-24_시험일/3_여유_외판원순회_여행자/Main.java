// 원문: 백준 2098 외판원 순회 (Gold 1, N <= 16). 백준 서비스 종료로 링크 없음.
// 같은 유형(바로 풀 수 있음): https://atcoder.jp/contests/abc180/tasks/abc180_e  (AtCoder ABC180 E, N <= 17)
// 눈으로 읽는 용도: 정답 풀이 + 설명 주석 + 예제 테스트. 실행: javac Main.java && java Main
// 문제: N개 도시, w[i][j] = i -> j 비용 (0이면 길 없음, 비대칭 가능).
//       모든 도시를 정확히 한 번씩 방문하고 출발 도시로 돌아오는 최소 비용.
import java.util.*;

class Solution {
    static final int INF = 1_000_000_000;   // Integer.MAX_VALUE는 더할 때 오버플로우
    int n;
    int[][] w;
    int[][] dp;                              // dp[현재 도시][방문한 도시 집합(비트마스크)]

    public int solution(int[][] cost) {
        n = cost.length;
        w = cost;
        dp = new int[n][1 << n];
        for (int[] row : dp) Arrays.fill(row, -1);   // -1 = 아직 계산 안 함
        return tsp(0, 1);                    // 0번 도시에서 출발, mask=1 (0번만 방문한 상태)
    }

    // cur에 서 있고 mask만큼 방문했을 때, 남은 도시를 다 돌고 0번으로 돌아가는 "남은" 최소 비용
    int tsp(int cur, int mask) {
        if (mask == (1 << n) - 1) {                      // 전부 방문 -> 0번으로 복귀
            return w[cur][0] != 0 ? w[cur][0] : INF;     // 돌아갈 길이 없으면 불가능(INF)
        }
        if (dp[cur][mask] != -1) return dp[cur][mask];   // 메모이제이션

        int res = INF;
        for (int next = 0; next < n; next++) {
            if ((mask & (1 << next)) != 0) continue;     // 이미 방문한 도시
            if (w[cur][next] == 0) continue;             // 길 없음
            int sub = tsp(next, mask | (1 << next));     // next로 가서 방문 표시
            if (sub >= INF) continue;                    // 그 뒤가 불가능하면 버림
            res = Math.min(res, sub + w[cur][next]);
        }
        return dp[cur][mask] = res;
    }
}

public class Main {
    static void check(String name, int expected, int actual) {
        if (expected != actual) throw new AssertionError(name + ": expected=" + expected + ", actual=" + actual);
        System.out.println("PASS " + name + " -> " + actual);
    }

    public static void main(String[] args) {
        // 백준 공식 예제. 최적 경로 0->1->3->2->0 = 10 + 10 + 9 + 6 = 35
        check("sample", 35, new Solution().solution(new int[][]{
                {0, 10, 15, 20}, {5, 0, 9, 10}, {6, 13, 0, 12}, {8, 8, 9, 0}}));
        check("N=2", 12, new Solution().solution(new int[][]{{0, 5}, {7, 0}}));
        check("N=3 cycle", 3, new Solution().solution(new int[][]{{0, 1, 100}, {100, 0, 1}, {1, 100, 0}}));
    }
}
