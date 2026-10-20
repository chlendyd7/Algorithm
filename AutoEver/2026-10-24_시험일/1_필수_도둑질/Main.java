// https://school.programmers.co.kr/learn/courses/30/lessons/42897

class Solution {
    public int solution(int[] money) {
        int n = money.length;
        int[] dp = new int[n];
        dp[0] = money[0];
        dp[1] = money[1];

        for (int i=2; i<n; i++) {
            dp[i] = Math.max(dp[i-2] + money[i], dp[i-1]);
        }
        // int answer = 0;
        return dp[n];
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        
        System.out.println(sol.solution());
    }
}
