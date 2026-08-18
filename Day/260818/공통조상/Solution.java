import java.util.*;

class Solution {
    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        
        for (int test_case = 1; test_case <= T; test_case++) {
            System.out.println("#" + test_case + " " + solve(sc));
        }
        sc.close();
    }
    
    static String solve(Scanner sc) {
        int[] parent;
        List<Integer>[] children;
        int V = sc.nextInt();
        int E = sc.nextInt();
        int S1 = sc.nextInt();
        int S2 = sc.nextInt();

        parent = new int[V + 1];

        List<Integer>[] tempChildren = new ArrayList[V + 1];
        children = tempChildren;
        for (int i = 0; i <= V; i++) {
            children[i] = new ArrayList<>();
        }

        for (int i = 0; i < E; i++) {
            int p = sc.nextInt();
            int c = sc.nextInt();
            parent[c] = p;
            children[p].add(c);
        }

        Set<Integer> ancestors = new HashSet<>();
        int current = S1;
        while (current != 0) {
            ancestors.add(current);
            current = parent[current];
        }

        current = S2;
        while (!ancestors.contains(current)) {
            current = parent[current];
        }
        int lca = current;

        int count = 0;
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(lca);

        while (!stack.isEmpty()) {
            int node = stack.pop();
            count++;
            for(int child : children[node]) {
                stack.push(child);
            }
        }

        return lca + " " + count;
    }
}
