import java.io.*;
import java.util.*;

public class Solution260216 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);
        int[][] dp = new int[102][102];
        for (int i=0; i<N; i++) {
            String[] pos = br.readLine().split(" ");
            int x1 = Integer.parseInt(pos[0]);
            int y1 = Integer.parseInt(pos[1]);
            int x2 = Integer.parseInt(pos[2]);
            int y2 = Integer.parseInt(pos[3]);

            dp[x1][y1] += 1;
            dp[x1][y2+1] -= 1;
            dp[x2+1][y1] -= 1;
            dp[x2+1][y2+1] += 1;
        }

        int result = 0;
        for (int i=1; i<101; i++) {
            for (int j=1; j<101; j++) {
                dp[i][j] += dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1];

                if (dp[i][j] > M) {
                    result ++;
                }
            }
        }
        System.out.println(result);
    }

}
