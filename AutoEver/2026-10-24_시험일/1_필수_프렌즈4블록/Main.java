// https://school.programmers.co.kr/learn/courses/30/lessons/17679
// 2×2 형태로 4개가 붙어있을 경우 사라지면서 점수를 얻는 게임이다.
import java.util.*;

class Solution {
    char [][] g;
    int m, n;
    public int solution(int m, int n, String[] board) {
        g = new char[m][n];
        this.m = m;
        this.n = n;

        for (int i=0; i<m; i++) g[i] = board[i].toCharArray();

        int answer = 0;
        int cnt;
        while((cnt = process()) > 0) {
            answer += cnt;
            drop();
        };
        return answer;
    }

    public int process() {
        boolean[][] pop = new boolean[m][n];
        for (int i=0; i<m-1; i++) {
            for (int j=0; j<n-1; j++) {
                char c = g[i][j];
                if (c !='.' 
                && c == g[i+1][j] 
                && c == g[i+1][j+1] 
                && c == g[i][j+1] 
                )
                pop[i][j] = pop[i+1][j] = pop[i+1][j+1] = pop[i][j+1] = true;
            }
        }
        int cnt = 0;
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (pop[i][j]) {g[i][j] = '.'; cnt++;}
            }
        }
        return cnt;
    }
    void drop() {
        for (int j=0; j<n; j++) {
            int w = m-1;
            for (int i=m-1; i>=0; i--) {
                if(g[i][j] != '.') {
                    char c = g[i][j];
                    g[i][j] = '.';
                    g[w--][j] = c;
                }
            }
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution(4,5,new String[] {"CCBDE", "AAADE", "AAABF", "CCBBF"}));
    }
}
