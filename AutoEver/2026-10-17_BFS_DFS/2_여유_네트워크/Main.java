// https://school.programmers.co.kr/learn/courses/30/lessons/43162

import java.util.*;

class Solution {
    int[] parent;
    
    public int solution(int n, int[][] computers) {
        init(n);
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                if (computers[i][j] == 1) {
                    union(i,j);
                }
            }
        }
        
        //해당 부분 더 정확한 방법
        int answer = 0;
        boolean[] visited = new boolean[n];
        for (int i = 0; i < n; i++) {
            int root = find(i); // 최상위 루트를 찾아서
            if (!visited[root]) { // 아직 방문하지 않은 루트라면
                visited[root] = true;
                answer++;
            }
        }
        return answer;
    }
    
    void init(int n) {
        parent = new int[n];
        for (int i=0; i<n; i++) parent[i] = i;
    }
    
    int find(int x) {
        if (parent[x] == x) return x;
        return parent[x] = find(parent[x]);
    }
    
    void union(int a, int b){
        a = find(a); b = find(b);
        if (a!=b) parent[a] = b;
    }
}


public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution());
    }
}
