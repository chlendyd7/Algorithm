// https://school.programmers.co.kr/learn/courses/30/lessons/92344
// 연습용: TODO를 구현하기 전에는 예제 실행 시 예외가 발생합니다.
import java.util.*;

class Solution {
    public int solution(int[][] board, int[][] skill) {
        // TODO: README의 조건을 확인하고 직접 구현하세요.
        throw new UnsupportedOperationException("TODO: 파괴되지 않은 건물");
    }
}

public class Main {
    static void check(int expected, int actual) {
        if (expected != actual) {
            throw new AssertionError("expected=" + expected + ", actual=" + actual);
        }
        System.out.println("PASS " + actual);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        check(10, sol.solution(new int[][]{
            {5,5,5,5,5}, {5,5,5,5,5}, {5,5,5,5,5}, {5,5,5,5,5}},
            new int[][]{{1,0,0,3,4,4}, {1,2,0,2,3,2}, {2,1,0,3,1,2}, {1,0,1,3,3,1}}));
        check(6, sol.solution(new int[][]{{1,2,3}, {4,5,6}, {7,8,9}},
            new int[][]{{1,1,1,2,2,4}, {1,0,0,1,1,2}, {2,2,0,2,0,100}}));
        // 자체 경계 예제: 내구도가 정확히 0이면 파괴.
        check(0, sol.solution(new int[][]{{1}}, new int[][]{{1,0,0,0,0,1}}));
        // 자체 경계 예제: 파괴된 건물도 회복 가능.
        check(1, sol.solution(new int[][]{{1}},
            new int[][]{{1,0,0,0,0,2}, {2,0,0,0,0,2}}));
    }
}

