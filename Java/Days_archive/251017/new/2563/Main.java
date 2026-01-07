import java.io.*;
import java.util.*;
/*
 * 크기가 10x10 정사각 모형임
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        boolean[][] paper = new boolean[100][100];

        int totalArea = 0;

        for (int k=0; k<N; k++) {
            String[] st = br.readLine().split(" ");
            int col = Integer.parseInt(st[0]);
            int row = Integer.parseInt(st[1]);

            int endCol = col + 10;
            int endRow = row + 10;

            for (int i=row; i<endRow; i++) {
                for (int j=col; j<endCol; j++) {
                    if (i>=0 && i< 100 && j>=0 && j<100) {
                        if (!paper[i][j]) {
                            paper[i][j] = true;
                            totalArea++;
                        }
                    }
                }
            }
        }
        System.out.println(totalArea);
    }
}
