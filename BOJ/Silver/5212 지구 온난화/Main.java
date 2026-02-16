import java.io.*;
import java.util.*;

public class Main {
    static int[] dr = {-1,1,0,0};
    static int[] dc = {0,0,-1,1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int R = Integer.parseInt(input[0]);
        int C = Integer.parseInt(input[1]);
        char[][] map = new char[R+2][C+2];
        for (int i=0; i<R+2; i++) {
            Arrays.fill(map[i], '.');
        }
        for (int i = 1; i < R+1; i++) {
            String line = br.readLine();
            for (int j=1; j< C+1; j++) {
                map[i][j] = line.charAt(j-1);
            }
        }
        char[][] newMap = new char[R+2][C+2];
        for (int i=0; i<R+2; i++) {
            Arrays.fill(newMap[i], '.');
        }

        for (int i=1; i< R+1; i++) {
            for (int j=1; j<C+1; j++) {
                if (map[i][j] == 'X') {
                    int cntWater = 0;
                    for (int d=0; d<4; d++) {
                        int nr = i + dr[d];
                        int nc = j + dc[d];
    
                        if (map[nr][nc] == '.') cntWater++;
                    }
                    if (cntWater < 3) {
                        newMap[i][j] = 'X';
                    }
                }
            }
        }
        System.out.println(Arrays.deepToString(newMap));
        int minR = R, maxR = 1;
        int minC = C, maxC = 1;
        boolean hasIsland = false;

        for (int i=1; i<R+1; i++) {
            for (int j=1; j<C+1; j++) {
                if (newMap[i][j] == 'X') {
                    hasIsland = true;
                    minR = Math.min(minR, i);
                    maxR = Math.max(maxR, i);
                    minC = Math.min(minC, j);
                    maxC = Math.max(maxC, j);
                }
            }
        }

        if (hasIsland) {
            for (int i = minR; i< maxR+1; i++) {
                for (int j = minC; j<=maxC; j++) {
                    System.out.print(newMap[i][j]);
                }
                System.out.println();
            }
        }
    }
}