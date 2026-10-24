// https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15OZ4qAPICFAYD
// 입력/출력만 제공. solve()만 구현. (SWEA 제출 시에는 클래스 이름을 Solution으로 바꿔야 함)
// 입력: 첫 줄 T. 각 케이스: N(고객 수), 다음에 회사 (x y), 집 (x y), 고객 N명 (x y) 순서로 2N+4개 정수.
// 거리 = |x1-x2| + |y1-y2|. 회사에서 출발해 고객 N명을 모두 방문하고 집으로 가는 최소 이동거리.
import java.util.*;

public class Solution {
    // company, home: {x, y}. customers[i]: {x, y}. 최소 이동거리를 반환.
    static int best;
    static int solve(int[] company, int[] home, int[][] customers) {
        best = Integer.MAX_VALUE;
        dfs(company, customers, new boolean[customers.length], 0, 0, home);
        return best;
        
    }
    static void dfs(int[] cur, int[][]c, boolean[] visited, int cnt, int dist, int[] home) {
        if (dist >= best) return;
        if (cnt == c.length) {
            best = Math.min(best, dist+ Math.abs(cur[0] - home[0]) + Math.abs(cur[1] - home[1]));
            return;
        }
        for (int i=0; i<c.length; i++) {
            if(visited[i]) continue;
            visited[i] = true;
            dfs(c[i], c, visited, cnt+1, dist+ Math.abs(cur[0] - c[i][0]) + Math.abs(cur[1] - c[i][1]), home);
            visited[i] = false;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        StringBuilder sb = new StringBuilder();
        for (int tc = 1; tc <= T; tc++) {
            int n = sc.nextInt();
            int[] company = {sc.nextInt(), sc.nextInt()};
            int[] home = {sc.nextInt(), sc.nextInt()};
            int[][] customers = new int[n][2];
            for (int i = 0; i < n; i++) {
                customers[i][0] = sc.nextInt();
                customers[i][1] = sc.nextInt();
            }
            sb.append('#').append(tc).append(' ').append(solve(company, home, customers)).append('\n');
        }
        System.out.print(sb);
    }
}
