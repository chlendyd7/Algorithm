// 2025 카카오 하반기 2차, Lv2 "선인장 숨기기" (프로그래머스 문제 번호는 저장한 HTML에 없음)
// 연습용: TODO 구현 전에는 실행 시 예외가 발생합니다.
// m x n 격자, h x w 크기 구역. drops[i]는 i+1번째 빗방울 좌표.
// "구역 안 칸이 처음 젖는 시각"이 가장 늦은 구역의 왼쪽 위 좌표 반환. 안 젖는 구역이 있으면 최우선.
// 동점이면 가장 위쪽 행, 그다음 가장 왼쪽 열. 제한: m*n <= 500,000.
// 힌트: 칸마다 "젖는 시각"(안 젖으면 drops.length+1)을 만들면 "h*w 창의 최솟값이 최대인 위치"를 찾는 문제가 된다.
//       브루트포스 O(m*n*h*w)는 그룹 #1(m,n<=50, 30%)만 통과.
import java.util.*;

class Solution {
    public int[] solution(int m, int n, int h, int w, int[][] drops) {
        // TODO
        throw new UnsupportedOperationException("TODO");
    }
}

public class Main {
    static int[][] d(int... a) {
        int[][] x = new int[a.length / 2][2];
        for (int i = 0; i < x.length; i++) { x[i][0] = a[2 * i]; x[i][1] = a[2 * i + 1]; }
        return x;
    }

    static void check(String name, int[] expected, int[] actual) {
        if (!Arrays.equals(expected, actual))
            throw new AssertionError(name + ": expected=" + Arrays.toString(expected) + ", actual=" + Arrays.toString(actual));
        System.out.println("PASS " + name + " -> " + Arrays.toString(actual));
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // 프로그래머스 공식 예제 6개
        check("ex1", new int[]{2, 2}, sol.solution(4, 5, 2, 2, d(0,0, 3,1, 1,3, 2,4, 1,1, 2,2, 2,3, 0,4)));
        check("ex2", new int[]{1, 1}, sol.solution(3, 3, 1, 1, d(0,0, 0,1, 0,2, 1,0)));
        check("ex3", new int[]{0, 0}, sol.solution(4, 6, 3, 4, d(1,2)));
        check("ex4", new int[]{3, 4}, sol.solution(4, 6, 1, 2, d(0,1, 0,3, 0,5, 1,1, 1,3, 1,5, 2,1, 2,3, 2,5, 3,1, 3,3, 3,5)));
        check("ex5", new int[]{0, 0}, sol.solution(2, 2, 2, 2, d(0,0, 0,1, 1,1, 1,0)));
        check("ex6", new int[]{0, 2}, sol.solution(4, 4, 3, 1, d(2,0, 1,3, 3,2, 0,1)));

        // 그룹 #2 대비: 700x700, 350x350 구역, 모든 칸에 비 (고정 시드). 브루트포스면 시간 초과.
        int m = 700, n = 700;
        List<int[]> cells = new ArrayList<>();
        for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) cells.add(new int[]{i, j});
        Collections.shuffle(cells, new Random(1));
        int[][] big = cells.toArray(new int[0][]);
        long t0 = System.currentTimeMillis();
        check("700x700", new int[]{0, 331}, sol.solution(m, n, 350, 350, big));
        System.out.println("time " + (System.currentTimeMillis() - t0) + "ms");

        // 1 x 500000 (m*n 한계, 한 줄), 비 1000방울
        Random q = new Random(2);
        int n2 = 500000, cnt = 1000;
        Set<Integer> s = new LinkedHashSet<>();
        while (s.size() < cnt) s.add(q.nextInt(n2));
        int[][] skinny = new int[cnt][2];
        int k = 0;
        for (int c : s) { skinny[k][0] = 0; skinny[k][1] = c; k++; }
        check("1x500000", new int[]{0, 126109}, sol.solution(1, n2, 1, 250000, skinny));
    }
}
