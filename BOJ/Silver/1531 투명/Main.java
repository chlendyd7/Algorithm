import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);
        int[][] dp = new int[101][101];
        int x1,y1,x2,y2;
        for (int i=0; i<N; i++) {
            String[] input2 = br.readLine().split(" ");
            x1 = Integer.parseInt(input2[0]);
            y1 = Integer.parseInt(input2[1]);
            x2 = Integer.parseInt(input2[2]);
            y2 = Integer.parseInt(input2[3]);
            for (int r=x1; r<x2+1; r++) {
                for (int c=y1; c<y2+1; c++) {
                    dp[r][c] += 1;
                }
            }
        }
        int result = 0;
        for (int i=0; i<101; i++) {
            for (int j=0; j<101; j++) {
                if (dp[i][j] > M) {
                    result ++;
                }
            }
        }
        System.out.print(result);
    }
}