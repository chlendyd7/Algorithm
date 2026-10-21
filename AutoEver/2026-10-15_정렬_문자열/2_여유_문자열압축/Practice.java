/*
    몇개인지 count
    이전꺼랑 비교

 */
class Solution {
    public int solution(String s) {
        int n = s.length();
        if(n == 1) return 1;
        int minLength = Integer.MAX_VALUE;
        
        for (int step=1; step<=n/2; step++) {
            String prev = s.substring(0, step);
            int count = 1;
            StringBuilder sb = new StringBuilder();

            for(int i=step; i<n; i+=step) {
                int end = Math.min(n, i+step);
                String curr = s.substring(i, end);

                if (prev.equals(curr)) {
                    count ++;
                } else {
                    if (count > 1) {
                        sb.append(count);
                    }
                    sb.append(prev);
                    prev = curr;
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


public class Practice {
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
