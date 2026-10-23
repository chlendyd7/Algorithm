// https://school.programmers.co.kr/learn/courses/30/lessons/42897

class Solution {
    public int solution(int[] money) {
        int n = money.length;
        // 경우1: 0 ~ n-2, 경우2: 1 ~ n-1
        return Math.max(rob(money, 0, n - 2), rob(money, 1, n - 1));
    }

    // money[from..to] 구간에서 인접한 집 안 터는 최대값
    int rob(int[] money, int from, int to) {
        int len = to - from + 1;
        int[] dp = new int[len];
        dp[0] = money[from];
        dp[1] = Math.max(money[from], money[from + 1]);
        for (int i = 2; i < len; i++) {
            dp[i] = Math.max(dp[i - 1], dp[i - 2] + money[from + i]);
        }
        return dp[len - 1];
    }
}