// https://school.programmers.co.kr/learn/courses/30/lessons/42897

class Solution {
    public int solution(int[] money) {
        int n = money.length;
        // int answer = 0;
        return Math.max(rob(money, 0, n-2), rob(money, 1, n-1));
    }
    int rob(int[] money, int from, int to) {
        int len = to - from + 1;
        int [] dp = new int[len];
        dp[0] = money[from];
        dp[1] = Math.max(dp[0], money[from+1]);
        for (int i=2; i<len; i++) {
            dp[i] = Math.max(dp[i-2] + money[from + i], dp[i-1]);
        }
        return dp[len-1];
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.solution());
    }
}
