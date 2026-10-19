// https://leetcode.com/problems/rotting-oranges/
// 연습용: TODO 구현 전에는 실행 시 예외가 발생합니다.
import java.util.*;

class Solution {
    public int orangesRotting(int[][] grid) {
        // TODO: 0=빈 칸, 1=신선한 오렌지, 2=썩은 오렌지. 매 분 썩은 오렌지의 상하좌우 신선한 오렌지가 썩는다.
        // 신선한 오렌지가 하나도 안 남을 때까지 걸리는 최소 분. 처음부터 신선한 게 없으면 0. 불가능하면 -1.
        // 멀티소스 BFS: 2인 칸을 전부 큐에 먼저 넣고 한 번에 시작. 신선한 개수를 세어 두고 썩을 때마다 감소.
        throw new UnsupportedOperationException("TODO: 멀티소스 BFS");
    }
}

public class Main {
    static void check(int expected, int actual) {
        if (expected != actual) throw new AssertionError("expected=" + expected + ", actual=" + actual);
        System.out.println("PASS " + actual);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        check(4, sol.orangesRotting(new int[][]{{2, 1, 1}, {1, 1, 0}, {0, 1, 1}}));
        check(-1, sol.orangesRotting(new int[][]{{2, 1, 1}, {0, 1, 1}, {1, 0, 1}}));
        check(0, sol.orangesRotting(new int[][]{{0, 2}}));
        check(0, sol.orangesRotting(new int[][]{{0}}));
        check(-1, sol.orangesRotting(new int[][]{{1}}));
    }
}
