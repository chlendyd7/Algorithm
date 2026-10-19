// https://school.programmers.co.kr/learn/courses/30/lessons/60057
// 연습용: TODO 구현 전에는 실행 시 예외가 발생합니다.
class Solution {
    public int solution(String s) {
        // TODO: 1..s.length()/2 길이로 앞에서부터 잘라 같은 덩어리가 연속되면 "개수+덩어리"로 압축.
        // 압축 후 문자열 길이의 최솟값 반환. 개수 1은 숫자를 쓰지 않는다. 개수가 두 자리 이상이면 자릿수도 길이에 포함.
        // 마지막에 남는 짧은 조각도 길이에 더한다. 길이 1 문자열 경계 확인.
        throw new UnsupportedOperationException("TODO: 문자열 압축");
    }
}

public class Main {
    static void check(int expected, int actual) {
        if (expected != actual) throw new AssertionError("expected=" + expected + ", actual=" + actual);
        System.out.println("PASS " + actual);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        check(7, sol.solution("aabbaccc"));
        check(9, sol.solution("ababcdcdababcdcd"));
        check(8, sol.solution("abcabcdede"));
        check(14, sol.solution("abcabcabcabcdededededede"));
        check(17, sol.solution("xababcdcdababcdcd"));
        check(1, sol.solution("a"));
    }
}
