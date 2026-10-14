import java.io.*;
import java.util.*;

public class Main {

    static int[][] board = new int[10][10];
    static int[] papers = { 0, 5, 5, 5, 5, 5 };
    static int minVal = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < 10; i++) {
            String[] line = br.readLine().split(" ");
            for (int j = 0; j < 10; j++) {
                board[i][j] = Integer.parseInt(line[j]);
            }
        }
        dfs(0, 0, 0);
        System.out.println(minVal == Integer.MAX_VALUE ? -1 : minVal);
        ;
    }

    static void dfs(int r, int c, int cnt) {
        if (r >= 9 && c >= 10) {
            minVal = Math.min(minVal, cnt);
            return;
        }

        if (c >= 10) {
            dfs(r + 1, 0, cnt);
            return;
        }
        if (cnt >= minVal) return;
        if (board[r][c] == 1) {
            for (int size = 5; size >= 1; size--) {
                if (papers[size] > 0 && canPlace(r, c, size)) {
                    updateBoard(r, cnt, size, 0);
                    papers[size]--;

                    dfs(r, c+1, cnt+1);
                    papers[size]++;
                    updateBoard(r, cnt, size, 1);
                }
            }
        }
    }

    static boolean canPlace(int r, int c, int size) {
        if (r + size > 10 || c + size > 10)
            return false;
        for (int i = r; i < r + size; i++) {
            for (int j = c; j < c + size; j++) {
                if (board[i][j] == 0)
                    return false;
            }
        }
        return true;
    }

    static void updateBoard(int r, int c, int size, int val) {
        for (int i = r; i < r + size; i++) {
            for (int j = c; j < c + size; j++) {
                
            }
        }
    }
}