// https://school.programmers.co.kr/learn/courses/30/lessons/67259
// 연습용: TODO 구현 전에는 실행 시 예외가 발생합니다.
import java.util.*;

class Solution {
    int[] dr = {-1, 1, 0, 0};   // 상 하 좌 우
    int[] dc = {0, 0, -1, 1};

    public int solution(int[][] board) {
        int n = board.length;
        int INF = Integer.MAX_VALUE;

        int[][][] dist = new int[n][n][4];
        for (int[][] a : dist) for (int[] b : a) Arrays.fill(b, INF);

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[3], b[3]));  // {r, c, dir, cost}
        for (int d = 0; d < 4; d++) {           // 시작은 4방향 모두 비용 0
            dist[0][0][d] = 0;
            pq.offer(new int[] {0, 0, d, 0});
        }

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int r = cur[0], c = cur[1], d = cur[2], cost = cur[3];
            if (cost > dist[r][c][d]) continue;     // 이미 더 좋은 값이 갱신된 낡은 항목

            for (int nd = 0; nd < 4; nd++) {
                int nr = r + dr[nd], nc = c + dc[nd];
                if (nr < 0 || nc < 0 || nr >= n || nc >= n || board[nr][nc] == 1) continue;

                int ncost = cost + 100 + (nd != d ? 500 : 0);   // 방향 바뀌면 코너 비용
                if (ncost < dist[nr][nc][nd]) {
                    dist[nr][nc][nd] = ncost;
                    pq.offer(new int[] {nr, nc, nd, ncost});
                }
            }
        }

        int ans = INF;
        for (int d = 0; d < 4; d++) ans = Math.min(ans, dist[n-1][n-1][d]);
        return ans;
    }
}

public class Main {
    static void check(int expected, int actual) {
        if (expected != actual) throw new AssertionError("expected=" + expected + ", actual=" + actual);
        System.out.println("PASS " + actual);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        check(900, sol.solution(new int[][]{{0, 0, 0}, {0, 0, 0}, {0, 0, 0}}));
        check(3800, sol.solution(new int[][]{
                {0, 0, 0, 0, 0, 0, 0, 1}, {0, 0, 0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 1, 0, 0}, {0, 0, 0, 0, 1, 0, 0, 0},
                {0, 0, 0, 1, 0, 0, 0, 1}, {0, 0, 1, 0, 0, 0, 1, 0}, {0, 1, 0, 0, 0, 1, 0, 0}, {1, 0, 0, 0, 0, 0, 0, 0}}));
        check(2100, sol.solution(new int[][]{{0, 0, 1, 0}, {0, 0, 0, 0}, {0, 1, 0, 1}, {1, 0, 0, 0}}));
        check(3200, sol.solution(new int[][]{
                {0, 0, 0, 0, 0, 0}, {0, 1, 1, 1, 1, 0}, {0, 0, 1, 0, 0, 0},
                {1, 0, 0, 1, 0, 1}, {0, 1, 0, 0, 0, 1}, {0, 0, 0, 0, 0, 0}}));
    }
}
