// 연습용: TODO 구현 전에는 실행 시 예외가 발생합니다.
// 후기의 DP 유형(백준 1149 RGB거리 모양) 대비. 같은 구조의 프로그래머스 땅따먹기(Lv2, 12913)도 함께.
// rgb : n개 집을 3색(빨강/초록/파랑) 중 하나로 칠한다. 인접한 집은 같은 색 금지. cost[i][c] = i번 집을 c색으로 칠하는 비용. 최소 총비용.
// land: n행 4열. 한 행에서 한 칸씩 고르되 바로 윗행에서 고른 열과 같은 열은 못 고름. 고른 값 합의 최댓값.
// 상태: dp[i][마지막으로 쓴 색/열]. 점화식에서 "직전과 다른 것"의 최솟값/최댓값을 취한다.
import java.util.*;

class Solution {
    public int rgb(int[][] cost) {
        // TODO
        throw new UnsupportedOperationException("TODO");
    }

    public int land(int[][] land) {
        // TODO
        throw new UnsupportedOperationException("TODO");
    }
}

public class Main {
    static void check(String name, int expected, int actual) {
        if (expected != actual) throw new AssertionError(name + ": expected=" + expected + ", actual=" + actual);
        System.out.println("PASS " + name + " -> " + actual);
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        check("rgb ex1", 96, s.rgb(new int[][]{{26, 40, 83}, {49, 60, 57}, {13, 89, 99}}));
        check("rgb ex2", 3, s.rgb(new int[][]{{1, 100, 100}, {100, 1, 100}, {100, 100, 1}}));
        check("rgb ex3", 208, s.rgb(new int[][]{{30, 19, 5}, {64, 77, 64}, {15, 19, 97}, {4, 71, 57}, {90, 86, 84}, {93, 32, 91}}));
        check("land ex1", 16, s.land(new int[][]{{1, 2, 3, 5}, {5, 6, 7, 8}, {4, 3, 2, 1}}));

        // 고정 시드 큰 입력
        Random q = new Random(1);
        int n = 1000;
        int[][] c = new int[n][3];
        for (int i = 0; i < n; i++) for (int j = 0; j < 3; j++) c[i][j] = 1 + q.nextInt(999);
        check("rgb 1000", 317107, s.rgb(c));

        Random q2 = new Random(2);
        int m = 100000;
        int[][] l = new int[m][4];
        for (int i = 0; i < m; i++) for (int j = 0; j < 4; j++) l[i][j] = 1 + q2.nextInt(100);
        check("land 100000", 7759431, s.land(l));
    }
}
