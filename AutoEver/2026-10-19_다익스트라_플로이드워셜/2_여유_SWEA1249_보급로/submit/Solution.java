// SWEA 제출용 (SWEA Java는 public class 이름이 Solution이어야 함)
import java.util.*;

public class Solution {
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};

    static int solve(int[][] map) {
        int n = map.length;
        int m = map[0].length;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));

        int[][] visited = new int[n][m];
        for (int[] a : visited) Arrays.fill(a, Integer.MAX_VALUE);
        visited[0][0] = 0;

        pq.add(new int[] {0, 0, 0});
        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int cost = curr[0], x = curr[1], y = curr[2];
            if (visited[x][y] < cost) continue;

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (0 <= nx && 0 <= ny && nx < n && ny < m) {
                    int nCost = cost + map[nx][ny];
                    if (visited[nx][ny] > nCost) {
                        visited[nx][ny] = nCost;
                        pq.add(new int[] {nCost, nx, ny});
                    }
                }
            }
        }
        return visited[n - 1][m - 1];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        StringBuilder sb = new StringBuilder();
        for (int tc = 1; tc <= T; tc++) {
            int n = sc.nextInt();
            int[][] map = new int[n][n];
            for (int i = 0; i < n; i++) {
                String row = sc.next();   // nextLine() 쓰면 남은 줄바꿈 때문에 빈 줄이 읽힘
                for (int j = 0; j < n; j++) map[i][j] = row.charAt(j) - '0';
            }
            sb.append('#').append(tc).append(' ').append(solve(map)).append('\n');
        }
        System.out.print(sb);
    }
}
