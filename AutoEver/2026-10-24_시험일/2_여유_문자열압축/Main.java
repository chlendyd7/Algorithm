// https://school.programmers.co.kr/learn/courses/30/lessons/60057
// 연습용: TODO 구현 전에는 실행 시 예외가 발생합니다.
class Solution {
    public int solution(String s) {
        int minLength = s.length();
        for (int step=1; step <= s.length()/2; step++) {
            StringBuilder sb = new StringBuilder();
            String prev = s.substring(0, step);
            
            int count = 1;
            for (int i=step; i<s.length(); i+=step) {
                int end = Math.min(s.length(), i+step);
                String sub = s.substring(i, end);
                
                if(prev.equals(sub)) {
                    count++;
                } else {
                    if (count > 1) {
                        sb.append(count);
                    }
                    sb.append(prev);
                    prev = sub;
                    count = 1;
                }
            }
            if (count > 1) {
                sb.append(count);
            }
            sb.append(prev);
            minLength = Math.min(minLength, sb.length());
        }
        
        return minLength;
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
