class Solution {
    int[] parent;

    int find(int a) {
        if (parent[a] != a) parent[a] = find(parent[a]);   // 경로 압축
        return parent[a];
    }

    public long solution(int[] x, int[] y, double e) {
        int n = x.length;

        // 1) 모든 섬 쌍의 간선 만들기: {L², i, j}
        List<long[]> edges = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {          // j = i+1부터: 같은 쌍 중복 방지
                long dx = x[i] - x[j], dy = y[i] - y[j];
                edges.add(new long[] {dx * dx + dy * dy, i, j});
            }
        }

        // 2) 비용 오름차순 정렬
        edges.sort((a, b) -> Long.compare(a[0], b[0]));

        // 3) Union-Find: 다른 그룹이면 연결
        parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;

        long total = 0;
        for (long[] ed : edges) {
            int a = find((int) ed[1]), b = find((int) ed[2]);
            if (a != b) {
                parent[a] = b;
                total += ed[0];
            }
        }
        return Math.round(total * e);
    }
}
