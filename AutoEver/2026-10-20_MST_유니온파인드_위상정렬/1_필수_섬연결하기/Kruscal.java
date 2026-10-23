import java.util.*;

class Solution {
    class UnionFind {
        int [] parent;
        int [] size;
        
        public UnionFind(int n) {
            parent = new int[n];
            size = new int[n];
            for (int i=0; i<n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }
        
        public int find(int x) {
            if (parent[x] == x) return x;
            return parent[x] = find(parent[x]);
        }
        
        public boolean union(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);
            if (rootX == rootY) return false;
            
            if (size[rootX] < size[rootY]) {
                int temp = rootX;
                rootX = rootY;
                rootY = temp;
            }
            
            parent[rootY] = rootX;
            size[rootX] += size[rootY];
            
            return true;
        }
        
    }
    
    record Node(int s, int e) {}
    public int solution(int n, int[][] costs) {
        Arrays.sort(costs, (a,b) -> Integer.compare(a[2], b[2]));
        UnionFind uf = new UnionFind(n);
        int answer = 0;
        int selected = 0;
        
        for (int[] node : costs) {
            int s = node[0];
            int e = node[1];
            int w = node[2];
            
            if (uf.union(s, e)) {
                answer += w;
                selected++;
                if (selected == n-1) {
                    break;
                }
            }
        }
        return answer;
    }
}