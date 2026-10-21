// https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15QRX6APsCFAYD
// 연습용: TODO 구현 전에는 실행 시 예외가 발생합니다.
// 입력 파싱은 Main이 해줌. solution()만 구현.
// (0,0) -> (N-1,N-1) 이동하며 "들어가는 칸의 숫자" 합이 복구시간. 최솟값 반환.
import java.util.*;

class Solution {
    int[] dx = {1,-1,0,0};
    int[] dy = {0,0,1,-1};

    public int solution(int[][] map) {
        // cost, a, b
        int n = map.length;
        int m = map[0].length;
        PriorityQueue<int[]> pq = new PriorityQueue<>(
            (a,b) -> Integer.compare(a[0], b[0])
        );

        int[][] visited = new int[n][m];
        for (int [] a: visited) Arrays.fill(a, Integer.MAX_VALUE);
        visited[0][0] = 0;

        pq.add(new int[] {0,0,0});
        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int cost = curr[0], x = curr[1], y = curr[2];
            if (visited[x][y] < cost) continue;

            for (int i=0; i<4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (0<=nx && 0<=ny && nx < n && ny < m) {
                    int nCost = cost + map[nx][ny];
                    if (visited[nx][ny] > nCost) {
                        visited[nx][ny] = nCost;
                        pq.add(new int[] {nCost, nx, ny});
                    }
                }
            }
        }

        return visited[n-1][m-1];


    }
}

public class Main {
    // "0100" 같은 문자열 줄들 -> int[][]
    static int[][] parse(String... rows) {
        int n = rows.length;
        int[][] map = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                map[i][j] = rows[i].charAt(j) - '0';
        return map;
    }

    static void check(String name, int expected, int actual) {
        if (expected != actual) throw new AssertionError(name + ": expected=" + expected + ", actual=" + actual);
        System.out.println("PASS " + name + " -> " + actual);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        check("4x4", 2, sol.solution(parse("0100", "1110", "1011", "1010")));
        check("6x6", 2, sol.solution(parse("011001", "010100", "010011", "101001", "010101", "111010")));
        check("1x1", 0, sol.solution(parse("0")));
        check("2x2", 9, sol.solution(parse("09", "90")));
        check("3x3 forced 9s", 27, sol.solution(parse("099", "999", "990")));
        check("3x3 all 0", 0, sol.solution(parse("000", "000", "000")));
        check("4x4 detour", 11, sol.solution(parse("0911", "0191", "1190", "9990")));

        // 100x100 (최대 크기): 시작/도착 0, 나머지 전부 1 -> 197칸 통과
        int N = 100;
        int[][] big = new int[N][N];
        for (int[] row : big) Arrays.fill(row, 1);
        big[0][0] = 0;
        big[N - 1][N - 1] = 0;
        long t0 = System.currentTimeMillis();
        check("100x100 all 1", 197, sol.solution(big));
        System.out.println("time " + (System.currentTimeMillis() - t0) + "ms");
    }
}
