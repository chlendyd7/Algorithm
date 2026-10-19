// https://school.programmers.co.kr/learn/courses/30/lessons/92335
// 연습용: TODO 구현 전에는 실행 시 예외가 발생합니다.
import java.util.*;

class Solution {
    public int solution(int n, int k) {
        // TODO: n을 k진수로 바꾼 문자열에서, '0'을 구분자로 자른 각 조각이 소수인 개수.
        // 조각 예: 211020101011 → 211, 2, 1, 1 (1은 소수 아님). 0 사이 빈 조각은 건너뛴다.
        // 조각을 Long.parseLong으로 읽는다. k=3이면 조각이 int 범위를 넘을 수 있다.
        // 소수 판별은 i*i <= x 까지 나눠 본다 (x는 long, i도 long).
        throw new UnsupportedOperationException("TODO: k진수 변환 + 소수 판별");
    }
}

public class Main {
    static void check(int expected, int actual) {
        if (expected != actual) throw new AssertionError("expected=" + expected + ", actual=" + actual);
        System.out.println("PASS " + actual);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        check(3, sol.solution(437674, 3));
        check(2, sol.solution(110011, 10));
        check(2, sol.solution(1000000, 3));
        check(0, sol.solution(1, 3));
    }
}
