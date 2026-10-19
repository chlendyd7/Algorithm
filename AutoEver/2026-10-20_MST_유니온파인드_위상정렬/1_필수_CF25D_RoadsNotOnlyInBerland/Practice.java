// https://codeforces.com/problemset/problem/25/D
// 연습용: 입출력 없이 solve()만 구현. 정답이 여러 개라 check()가 "유효한지"만 검사한다.
// 실행: javac Practice.java && java Practice
import java.util.*;

public class Practice {
    static class UnionFind {
        int[] parent;
        int count;

        public UnionFind(int n) {
            parent = new int[n];
            for (int i=0; i<n; i++) {parent[i] = i;}
            count = n;
        
        }
        public int find(int i) {
            if (parent[i] == i) return i;
            return parent[i] = find(parent[i]);
        }
        public boolean union(int a, int b) {
            int rootA = find(a);
            int rootB = find(b);
            if (rootA != rootB) {
                parent[rootA] = rootB;
                count --;
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

    // n: 도시 수(1..n), roads: n-1개의 {u, v}
    // 반환: 하루마다 {닫을 u, 닫을 v, 지을 a, 지을 b}. 하루도 필요 없으면 길이 0 배열.
    static int[][] solve(int n, int[][] roads) {
        UnionFind uf = new UnionFind(n+1);
        List<Edge> extraEdges = new ArrayList<>();
        for (int[] r : roads) {
            int u = r[0];
            int v = r[1];

            if (!uf.union(u, v)) {
                extraEdges.add(new Edge(u, v));
            }
        }

        List<Integer> roots = new ArrayList<>();
        for (int i=1; i<n+1; i++) {
            if (uf.find(i) == i) {
                roots.add(i);
            }
        }

        int t = roots.size()-1;
        int[][] ans = new int[t][4];
        for (int i = 0; i < t; i++) {
            Edge e = extraEdges.get(i);
            ans[i] = new int[] {e.u, e.v, roots.get(i), roots.get(i + 1)};
        }
    return ans;
    }

    // ---------- 채점 (수정 불필요) ----------
    static long key(int a, int b) {
        return (long) Math.min(a, b) * 1_000_000L + Math.max(a, b);
    }

    static void check(String name, int n, int[][] roads) {
        int[][] ans = solve(n, roads);

        // 1. 일수가 최소인가 (= 처음 컴포넌트 수 - 1)
        UnionFind init = new UnionFind(n + 1);
        for (int[] r : roads) init.union(r[0], r[1]);
        int expected = init.count - 2;      // 0번 노드가 혼자 1개를 차지하므로 -1 추가
        if (ans.length != expected)
            throw new AssertionError(name + ": t=" + ans.length + ", expected=" + expected);

        // 2. 하루씩 시뮬레이션: 닫는 도로는 실제 존재해야 함
        Set<Long> edges = new HashSet<>();
        for (int[] r : roads) edges.add(key(r[0], r[1]));
        for (int[] op : ans) {
            if (!edges.remove(key(op[0], op[1])))
                throw new AssertionError(name + ": 없는 도로를 닫음 " + Arrays.toString(op));
            if (op[2] == op[3])
                throw new AssertionError(name + ": 자기 자신으로 도로를 지음 " + Arrays.toString(op));
            edges.add(key(op[2], op[3]));
        }

        // 3. 끝난 뒤 전부 연결되었는가
        UnionFind fin = new UnionFind(n + 1);
        for (long e : edges) fin.union((int) (e / 1_000_000L), (int) (e % 1_000_000L));
        if (fin.count != 2)
            throw new AssertionError(name + ": 아직 연결 안 됨, 덩어리 수=" + (fin.count - 1));

        System.out.println("PASS " + name + " t=" + ans.length);
    }

    public static void main(String[] args) {
        check("이미 트리", 3, new int[][]{{1, 2}, {2, 3}});
        check("두 도시", 2, new int[][]{{1, 2}});
        check("사이클 1개 + 고립 1개", 4, new int[][]{{1, 2}, {2, 3}, {3, 1}});
        check("덩어리 2개", 5, new int[][]{{1, 2}, {2, 3}, {3, 1}, {4, 5}});
        check("덩어리 3개", 7, new int[][]{{1, 2}, {2, 3}, {3, 1}, {4, 5}, {5, 6}, {6, 4}});
    }
}
