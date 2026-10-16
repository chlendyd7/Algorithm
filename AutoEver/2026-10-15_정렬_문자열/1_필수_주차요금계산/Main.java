// https://school.programmers.co.kr/learn/courses/30/lessons/92341
// 연습용: TODO를 구현하기 전에는 예제 실행 시 예외가 발생합니다.
import java.util.*;

class Solution {
    public int[] solution(int[] fees, String[] records) {
        // TODO: README의 조건을 확인하고 직접 구현하세요.
        throw new UnsupportedOperationException("TODO: 주차 요금 계산");
    }
}

public class Main {
    static void check(int[] expected, int[] actual) {
        if (!Arrays.equals(expected, actual)) {
            throw new AssertionError("expected=" + Arrays.toString(expected)
                + ", actual=" + Arrays.toString(actual));
        }
        System.out.println("PASS " + Arrays.toString(actual));
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        check(new int[]{14600, 34400, 5000}, sol.solution(
            new int[]{180, 5000, 10, 600},
            new String[]{"05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT",
                "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
                "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"}));
        check(new int[]{0, 591}, sol.solution(new int[]{120, 0, 60, 591},
            new String[]{"16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT",
                "18:00 0202 OUT", "23:58 3961 IN"}));
        check(new int[]{14841}, sol.solution(new int[]{1, 461, 1, 10},
            new String[]{"00:00 1234 IN"}));
    }
}

