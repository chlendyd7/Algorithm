import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        
        
        boolean[][] board = new boolean[100][100];
        int row, col;
        int result = 0;
        while (N > 0) {
            String[] input = br.readLine().split(" ");
            row = Integer.parseInt(input[0]);
            col = Integer.parseInt(input[1]);
            for (int i=row; i<row+10; i++) {
                for (int j=col; j<col+10; j++) {
                    if (!board[i][j]) {
                        result ++;
                        board[i][j] = true;
                    }
                }
            }
            N--;
        }
        System.out.println(result);
    }
}