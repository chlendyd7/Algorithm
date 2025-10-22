import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);

        int [][] A = new int[N][M];
        int [][] B = new int[N][M];

        for (int i=0; i<N; i++) {
            String[] row = br.readLine().split(" ");
            for (int j=0; j<M; j++) {
                A[i][j] = Integer.parseInt(row[j]);
            }
        }
        for (int i=0; i<N; i++) {
            String[] row = br.readLine().split(" ");
            for (int j=0; j<M; j++) {
                B[i][j] = Integer.parseInt(row[j]);
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                sb.append(A[i][j] + B[i][j]).append(" ");
            }
            sb.append("\n");
        }
        System.out.print(sb.toString());
    }
}