// https://school.programmers.co.kr/learn/courses/30/lessons/67258
// 연습용: TODO를 구현하기 전에는 예제 실행 시 예외가 발생합니다.
import java.util.*;

class Solution {
    public int[] solution(String[] gems) {
        // TODO: README의 조건을 확인하고 직접 구현하세요.
        throw new UnsupportedOperationException("TODO: 보석 쇼핑");
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
        check(new int[]{3, 7}, sol.solution(new String[]{
            "DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"}));
        check(new int[]{1, 3}, sol.solution(new String[]{"AA", "AB", "AC", "AA", "AC"}));
        check(new int[]{1, 1}, sol.solution(new String[]{"XYZ", "XYZ", "XYZ"}));
        check(new int[]{1, 5}, sol.solution(new String[]{"ZZZ", "YYY", "NNNN", "YYY", "BBB"}));
    }
}

