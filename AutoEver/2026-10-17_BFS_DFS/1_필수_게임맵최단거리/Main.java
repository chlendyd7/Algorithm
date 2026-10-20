// https://school.programmers.co.kr/learn/courses/30/lessons/1844

import java.util.*;

class Solution {
    int[][] dir = {
        {1,0}, {0,1}, {-1,0}, {0,-1}
    };
    
    public int solution(int[][] maps) {
        boolean[][] visited = new boolean[maps.length][maps[0].length];
        Deque<int[]> q = new ArrayDeque<>();
        q.offer(new int[] {0,0,1});
        visited[0][0] = true;
        
        while (!q.isEmpty()) {
            int [] curr = q.poll();
            int x = curr[0];
            int y = curr[1];
            if (x == maps.length-1 && y == maps[0].length-1) {
                return curr[2];
            }
            for (int i=0; i<dir.length; i++) {
                int nextX = x + dir[i][0];
                int nextY = y + dir[i][1];
                
                if (nextX > -1 && nextX < maps.length && nextY>-1 && nextY<maps[0].length) {
                    if (visited[nextX][nextY] == false && maps[nextX][nextY] == 1) {
                        visited[nextX][nextY] = true;
                        q.offer(new int[] {nextX, nextY, curr[2] + 1});
                    }
                }
            }
        }
        
        int answer = -1;
        return answer;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution());
    }
}
