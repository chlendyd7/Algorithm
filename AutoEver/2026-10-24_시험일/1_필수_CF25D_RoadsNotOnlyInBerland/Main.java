// https://codeforces.com/problemset/problem/25/D

import java.util.*;

public class Main {
    static class UnionFind {
        int[] parent;
        int count;
 
        public UnionFind(int n) {
            parent = new int[n];
            for (int i = 0; i < n; i++) parent[i] = i;
            count = n;
        }
        public int find(int i) {
            if (parent[i] == i) return i;
            return parent[i] = find(parent[i]);
        }
        public boolean union(int i, int j) {
            int rootI = find(i);
            int rootJ = find(j);
            if (rootI != rootJ) {
                parent[rootI] = rootJ;
                count--;
                return true;
            }
            return false;
        }
    }
 
    static class Edge {
        int u, v;
        public Edge(int u, int v) {
            this.u = u;
            this.v = v;
        }
    }
 
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
 
        UnionFind uf = new UnionFind(n + 1); // 1부터 n까지 번호 사용
        List<Edge> extraEdges = new ArrayList<>(); // 없애야 할 중복 도로 목록
 
        for (int i = 0; i < n - 1; i++) {
            String[] input = br.readLine().split(" ");
            int u = Integer.parseInt(input[0]);
            int v = Integer.parseInt(input[1]);
 
            // 이미 연결되어 있다면 사이클(중복 도로) 발생 -> 폐쇄 후보
            if (!uf.union(u, v)) {
                extraEdges.add(new Edge(u, v));
            }
        }
 
        // 1번 노드부터 끝까지 탐색하며 각 컴포넌트의 대표(루트) 노드들을 수집
        List<Integer> roots = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (uf.find(i) == i) {
                roots.add(i);
            }
        }
 
        // 필요한 일수(t)는 (컴포넌트 개수 - 1) 개
        int t = roots.size() - 1;
        StringBuilder sb = new StringBuilder();
        sb.append(t).append("\n");
 
        // 부서진 도로 하나와 새로운 연결선 하나를 짝지어서 출력
        for (int i = 0; i < t; i++) {
            Edge extra = extraEdges.get(i);
            int root1 = roots.get(i);
            int root2 = roots.get(i + 1);
 
            sb.append(extra.u).append(" ").append(extra.v)
              .append(" ").append(root1).append(" ").append(root2).append("\n");
        }
 
        System.out.print(sb);
    }
}