import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line = br.readLine().split(" ");
        int N = Integer.parseInt(line[0]);
        int M = Integer.parseInt(line[1]);
        
        int[][] board = new int[N][M];
        for(int i=0; i<N; i++) {
            String[] row = br.readLine().split(" ");
            for(int j=0; j<M; j++) {
                board[i][j] = Integer.parseInt(row[j]);
            }
        }
        int T = Integer.parseInt(br.readLine());
        
        int cnt = 0;
        int[] temp = new int[9]; // 리스트 대신 크기 9의 배열 재사용

        for (int i = 0; i <= N - 3; i++) {
            for (int j = 0; j <= M - 3; j++) {
                int idx = 0;
                // 3x3 영역 채우기
                for (int r = i; r < i + 3; r++) {
                    for (int c = j; c < j + 3; c++) {
                        temp[idx++] = board[r][c];
                    }
                }
                Arrays.sort(temp); // 매번 9개만 정렬하므로 매우 빠름
                if (temp[4] >= T) cnt++;
            }
        }
        System.out.println(cnt);
    }
}