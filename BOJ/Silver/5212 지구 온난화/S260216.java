import java.io.*;
import java.util.*;

public class S260216 {
    static int[] dr = {-1,1,0,0};
    static int[] dc = {0,0,-1,1};
    private static boolean isValid(int r, int c, int R, int C) {
        return r>=0 && r < R && c >=0 && c<C;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int R = Integer.parseInt(input[0]);
        int C = Integer.parseInt(input[1]);

        char[][] board = new char[R][C];
        char[][] newMap = new char[R][C];
        for (int i=0; i<R; i++) {
            String line = br.readLine();
            for (int j=0; j<C; j++) {
                board[i][j] = line.charAt(j);
            }
            Arrays.fill(newMap[i], '.');
        }

        for (int i=0; i<R; i++) {
            for (int j=0; j<C; j++) {
                if (board[i][j] == 'X') {
                    int cnt = 0;
                    for (int d=0; d<4; d++) {
                        int nx = i+dr[d];
                        int ny = j+dc[d];

                        if (isValid(nx, ny, R, C)) {
                            if (board[nx][ny] == '.') cnt++;
                        }
                    }
                    if (cnt < 3) {
                        newMap[i][j] = 'X';
                    }
                }
            }
        }
        int minR = R, maxR = 1;
        int minC = C, maxC = 1;
        boolean hasIsland = false;

        for (int i=0; i<R; i++) {
            for (int j=0; j<C; j++) {
                if (newMap[i][j] == 'X') {
                    hasIsland = true;
                    minR = Math.min(minR, i);
                    maxR = Math.max(maxR, i);
                    minC = Math.min(minC, j);
                    maxC = Math.max(maxC, j);
                }
            }
        }

        if(hasIsland) {
            for (int i=minR; i<maxR+1; i++) {
                for (int j=minC; j<maxC; j++) {
                    System.out.print(newMap[i][j]);
                }
                System.out.println();
            }
        }
    }
}