// https://codeforces.com/problemset/problem/25/D

import java.util.*;

public class Main {
    class UnionFind {
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
                parent[rootI] = rootJ;
                count--;
                return true;
            }
            return false;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

    }
}
