import java.io.*;
import java.util.*;


class Main {
    static int n, ans;
    static int[][] board;
    static boolean[][][] seen; // [mast][last][price]

    static void dfs(int mask, int last, int price) {
        if (seen[mask][last][price]) return;
        seen[mask][last][price] = true;
        ans = Math.max(ans, Integer.bitCount(mask));

        for (int next = 0; next < n; next++) {
            if ((mask & (1 << next)) != 0) continue;       // 이미 소유했던 사람
            int p = board[last][next];
            if (p < price) continue;                       // 산 가격보다 싸게 못 팖
            dfs(mask | (1 << next), next, p);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine().trim());
        board = new int[n][n];
        for (int i=0; i<n; i++) {
            String line = br.readLine().trim();
            for (int j=0; j<n; j++) {
                board[i][j] = line.charAt(j) - '0';
            }
        }
        seen = new boolean[1<<n][n][10];
        dfs(1,0,0);
        System.out.println(ans);

    }
}
