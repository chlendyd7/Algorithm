// https://school.programmers.co.kr/learn/courses/30/lessons/77485
// 연습용: TODO 구현 전에는 실행 시 예외가 발생합니다.
import java.util.*;

class Solution {
    public int[] solution(int rows, int columns, int[][] queries) {
        // TODO: 숫자는 행 우선으로 1..rows*columns. query는 1-based [x1,y1,x2,y2].
        // 각 query마다 직사각형 테두리를 시계방향으로 한 칸 회전하고, 움직인 숫자 중 최솟값을 query 순서대로 반환.
        // 회전 결과는 다음 query에 누적된다. 모서리 값을 임시 저장해야 덮어쓰기를 피한다.
        throw new UnsupportedOperationException("TODO: 행렬 테두리 회전");
    }
}

public class Main {
    static void check(int[] expected, int[] actual) {
        if (!Arrays.equals(expected, actual)) {
            throw new AssertionError("expected=" + Arrays.toString(expected) + ", actual=" + Arrays.toString(actual));
        }
        System.out.println("PASS " + Arrays.toString(actual));
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        check(new int[]{8, 10, 25}, sol.solution(6, 6, new int[][]{{2,2,5,4}, {3,3,6,6}, {5,1,6,3}}));
        check(new int[]{1, 1, 5, 3}, sol.solution(3, 3, new int[][]{{1,1,2,2}, {1,2,2,3}, {2,1,3,2}, {2,2,3,3}}));
        check(new int[]{1}, sol.solution(100, 97, new int[][]{{1,1,100,97}}));
    }
}
