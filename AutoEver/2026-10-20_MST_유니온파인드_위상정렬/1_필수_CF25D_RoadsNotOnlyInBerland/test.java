import java.util.*;

public class Main {
    static class UnionFind {
        int[] parent;
        int count;

        public UnionFind(int n) {
            parent = new int[n];
            for (int i=0; i<n; i++) parent[i] = i;
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
                parent[rootJ] = rootI;
                count--;
                return true;
            }
            return false;
        }
    }
    
    class Edge {
        int u, v;
        public Edge(int u, int v) {
            this.u = u;
            this.v = v;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        UnionFind uf = new UnionFind(n+1);
        List<Edge> extraEdges = new ArrayList<>();

        for (int i=0; i<n-1; i++) {
            String[] input = br.readline().split(" ");
            int u = Integer.parseInt(input[0]);
            int v = Integer.parseInt(input[1]);

            if(!uf.union(u,v)) {
                extraEdges.add(new Edge(u,v));
            }
        }
        
        List<Integer> roots = new ArrayList<>();
        for (int i=1; i<=n; i++) {
            if (uf.find(i) == i) {
                roots.add(i);
            }
        }

        int t = roots.size() -1;
        StringBuilder sb = new StringBuilder();
        sb.append(t).append("\n");

        for (int i=0; i<t; i++) {
            Edge extra = extraEdges.get(i);
            int root1 = roots.get(i);
            int root2 = roots.get(i+1);

            sb.append(extra.u).append(" ").append(extra.v)
              .append(" ").append(root1).append(" ").append(root2).append("\n");
        
        }

    }
}