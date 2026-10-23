// 자체 문제 (후기: "그래프가 나뉘어져 있는 경우와 사이클인 경우를 고려해야 하는 DFS 문제", "순환이면 홀/짝에 따라 n/2")를 바탕으로 만든 연습용
// 연습용: TODO 구현 전에는 실행 시 예외가 발생합니다.
// 무방향 그래프, 노드 0..n-1. 각 연결요소는 "일직선(경로)" 또는 "단순 사이클(길이 3 이상)" 중 하나. 자기 자신/중복 간선 없음.
// 각 노드에 대해 "같은 연결요소 안에서 가장 먼 노드까지의 최단거리"를 배열로 반환. 혼자인 노드는 0.
// 제한: n <= 200,000. 재귀 DFS는 깊이 10만이면 StackOverflow -> 반복문(스택/큐)으로.
// 힌트: 요소의 정점 수 V, 간선 수 E를 센다. E = V-1 이면 경로, E = V 이면 사이클.
//       사이클(길이 k)이면 모두 k/2 (정수 나눗셈). 경로면 끝점에서부터 순서를 매겨 max(i, k-1-i).
import java.util.*;

class Solution {
    public int[] solution(int n, int[][] edges) {
        // TODO
        throw new UnsupportedOperationException("TODO");
    }
}

public class Main {
    static void check(String name, int[] expected, int[] actual) {
        if (!Arrays.equals(expected, actual))
            throw new AssertionError(name + ": expected=" + Arrays.toString(expected) + ", actual=" + Arrays.toString(actual));
        System.out.println("PASS " + name + " -> " + (actual.length <= 12 ? Arrays.toString(actual) : "n=" + actual.length));
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        check("1 single", new int[]{0}, sol.solution(1, new int[][]{}));
        check("2 two nodes", new int[]{1, 1}, sol.solution(2, new int[][]{{0, 1}}));
        check("3 path of 5", new int[]{4, 3, 2, 3, 4}, sol.solution(5, new int[][]{{0, 1}, {1, 2}, {2, 3}, {3, 4}}));
        check("4 cycle of 5", new int[]{2, 2, 2, 2, 2}, sol.solution(5, new int[][]{{0, 1}, {1, 2}, {2, 3}, {3, 4}, {4, 0}}));
        check("5 cycle of 3", new int[]{1, 1, 1}, sol.solution(3, new int[][]{{0, 1}, {1, 2}, {2, 0}}));
        check("6 cycle of 4", new int[]{2, 2, 2, 2}, sol.solution(4, new int[][]{{0, 1}, {1, 2}, {2, 3}, {3, 0}}));
        // 경로 0-1-2, 사이클 3-4-5-6, 혼자 7
        check("7 mixed", new int[]{2, 1, 2, 2, 2, 2, 2, 0},
                sol.solution(8, new int[][]{{0, 1}, {1, 2}, {3, 4}, {4, 5}, {5, 6}, {6, 3}}));
        // 라벨이 섞인 경로: 2-0-3-1
        check("8 scrambled path", new int[]{2, 3, 3, 2}, sol.solution(4, new int[][]{{2, 0}, {0, 3}, {3, 1}}));

        // n = 200,000: 경로 100,000개 + 사이클 99,999개 + 혼자 1개, 라벨은 섞음 (고정 시드)
        int P = 100000, C = 99999, n = P + C + 1;
        int[] perm = new int[n];
        for (int i = 0; i < n; i++) perm[i] = i;
        Random r = new Random(1);
        for (int i = n - 1; i > 0; i--) { int j = r.nextInt(i + 1); int t = perm[i]; perm[i] = perm[j]; perm[j] = t; }
        List<int[]> el = new ArrayList<>();
        for (int i = 0; i + 1 < P; i++) el.add(new int[]{perm[i], perm[i + 1]});
        for (int i = 0; i < C; i++) el.add(new int[]{perm[P + i], perm[P + (i + 1) % C]});
        Collections.shuffle(el, r);
        int[] expected = new int[n];
        for (int i = 0; i < P; i++) expected[perm[i]] = Math.max(i, P - 1 - i);
        for (int i = 0; i < C; i++) expected[perm[P + i]] = C / 2;
        expected[perm[n - 1]] = 0;
        long t0 = System.currentTimeMillis();
        check("9 big", expected, sol.solution(n, el.toArray(new int[0][])));
        System.out.println("time " + (System.currentTimeMillis() - t0) + "ms");
    }
}
