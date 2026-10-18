// 원본: https://school.programmers.co.kr/learn/courses/30/lessons/42861
// 자체 변형: 온라인 judge 없음. README의 세 가지 조건을 구별하세요.
// 연습용: TODO 구현 전에는 실행 시 예외가 발생합니다.
import java.util.*;

class Solution {
    record Node (int target, int weight) {};

    public long additionalCost(int n, int[][] costs, int[][] preconnected) {
        List<List<Node>> graph = new ArrayList<>();
        for (int i=0; i<n; i++) graph.add(new ArrayList<>());
        for (int i=0; i<costs.length; i++) {
            int s = costs[i][0];
            int e = costs[i][1];
            int w = costs[i][2];
            
            graph.get(s).add(new Node(e, w));
            graph.get(e).add(new Node(s, w));
        }
        
        for (int i=0; i<preconnected.length; i++){
            int s = costs[i][0];
            int e = costs[i][1];
            int w = 0;
            
            graph.get(s).add(new Node(e, w));
            graph.get(e).add(new Node(s, w));
        }

        boolean[] visited = new boolean[n];
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) -> a[0] - b[0]);
        pq.add(new int[] {0,0});
        
        int totalCost = 0;
        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int weight = curr[0], node = curr[1];
            if (visited[node]) continue;
            visited[node] = true;
            totalCost += weight;
            
            for(Node edge: graph.get(node)) {
                int next = edge.target(), w = edge.weight();
                if (!visited[next]) pq.offer(new int[] {w, next});
            }
        }
        
        return totalCost;

        // TODO A: preconnected는 이미 설치된 무료 연결. 새로 설치할 최소 비용.
        // 연결 불가능하면 -1. costs의 노드 번호는 0-based.
        // throw new UnsupportedOperationException("TODO A: 이미 연결된 쌍");
    }
    static class UnionFind{
        int[] parent;
        int count;

        public UnionFind(int n) {
            parent = new int[n];
            for (int i=0; i<n; i++) parent[i] = i;
            count = n;
        }
        public int find(int i) {
            if (parent[i]==i) return i;
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

    public long requiredCost(int n, int[][] costs, int[] requiredEdgeIndices, boolean requireTree) {
        // TODO B/C: costs에서 지정된 간선은 반드시 설치하고 비용도 모두 합산.
        // requiredEdgeIndices는 costs의 0-based 인덱스. costs 정렬 전에 식별자를 보존.
        // requireTree=true이면 필수 간선의 사이클도 불가능(-1).
        UnionFind uf = new UnionFind(n);
        boolean[] isRequired = new boolean[costs.length];
        for (int idx: requiredEdgeIndices) {
            isRequired[idx] = true;
        }

        for (int idx: requiredEdgeIndices) {
            int u = costs[idx][0];
            int v = costs[idx][1];
            int w = costs[idx][2];

            totalCost += w;
            boolean united = uf.union(u,v);

            if(requiredTree && !united) {
                return -1;
            }
        }
        
        List<int[]> remainingEdges = new ArrayList<>();
        for (int i=0; i<costs.length; i++) {
            if (!isRequired[i]) {
                remainingEdges.add(costs[i]);
            }
        }
        
        remainingEdges.sort((a,b) -> Integer.compare(a[2], b[2]));
        for (int[] edges: remainingEdges) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];

            if (uf.union(u, v)) {
                totalCost += w;
            }
        }

        if (uf.count != 1) {
            return -1;
        }
        
        return totalCost;
    }
}

public class Main {
    static void check(long expected, long actual) {
        if (expected != actual) {
            throw new AssertionError("expected=" + expected + ", actual=" + actual);
        }
        System.out.println("PASS " + actual);
    }

    static int[][] costs() {
        // 매 호출 새 배열을 반환: 풀이가 정렬해도 다음 예제 간선 인덱스가 유지됨.
        return new int[][]{{0,1,1}, {1,2,2}, {2,3,3}, {0,3,10}, {0,2,8}};
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        check(3, sol.additionalCost(4, costs(), new int[][]{{0,3}}));
        check(0, sol.additionalCost(4, costs(), new int[][]{{0,1}, {1,2}, {2,3}}));
        check(6, sol.additionalCost(4, costs(), new int[0][2]));
        check(13, sol.requiredCost(4, costs(), new int[]{3}, true));
        check(14, sol.requiredCost(4, costs(), new int[]{0,1,4}, false));
        check(-1, sol.requiredCost(4, costs(), new int[]{0,1,4}, true));
        check(-1, sol.additionalCost(4, new int[][]{{0,1,1}, {2,3,1}}, new int[0][2]));
        check(0, sol.additionalCost(1, new int[0][3], new int[0][2]));
        check(3_000_000_000L, sol.additionalCost(4, new int[][]{
            {0,1,1_000_000_000}, {1,2,1_000_000_000}, {2,3,1_000_000_000}}, new int[0][2]));
    }
}
