import java.io.*;
import java.util.*;


class Main {
    static int n, ans;
    static int[][] board;
    static boolean seen[][][];

    static void dfs(int mask, int last, int cost) {
        if (seen[mask][last][cost]) return;
        seen[mask][last][cost] = true;
        ans = Math.max(ans, Integer.bitCount(mask));

        for (int i=0; i<n; i++) {
            if((mask & (1<<i)) != 0) continue;
            int p = board[last][i];
            if(p < cost) continue;
            dfs(mask | (1<<i), i, p);
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