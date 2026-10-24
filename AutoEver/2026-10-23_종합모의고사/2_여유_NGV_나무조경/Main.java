import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static boolean[] used;
    static int answer = 0;
    static List<Pair> pairs = new ArrayList<>();

    static class Pair {
        int first;
        int second;
        int score;

        Pair(int first, int second, int score) {
            this.first = first;
            this.second = second;
            this.score = score;
        }
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        int[][] board = new int[n][n];
        used = new boolean[n*n];
        
        for (int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                board[i][j] = sc.nextInt();
            }
        }

        for (int r=0; r<n; r++) {
            for (int c=0; c<n; c++) {
                int current = r*n+c;
                if(c+1<n) {
                    pairs.add(new Pair(
                        current,
                        r*n+(c+1),
                        board[r][c] + board[r][c+1]
                    ));
                }
                if (r+1 < n) {
                    pairs.add(new Pair(
                        current,
                        (r+1) * n + c,
                        board[r][c] + board[r+1][c]
                    ));
                }
            }
        }

        dfs(0,0,0);
        System.out.println(answer);
    }
    static void dfs(int start, int count, int sum) {
        answer = Math.max(answer, sum);
        if (count==4) {
            return;
        }

        for (int i=start; i<pairs.size(); i++) {
            Pair pair = pairs.get(i);
            if(used[pair.first] || used[pair.second]) {
                continue;
            }
            used[pair.first] = true;
            used[pair.second] = true;

            dfs(i+1, count+1, sum+pair.score);
  
            used[pair.first] = false;
            used[pair.second] = false;
            
        }
    }
}
