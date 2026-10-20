// https://school.programmers.co.kr/learn/courses/30/lessons/43238

class Solution {
    public long solution(int n, int[] times) {
        long left = 1;
        long right = (long) Arrays.stream(times).max().getAsInt() * n;
        long answer = right;
        while (left <= right) {
            long mid = (left + right) / 2;
            long temp = 0;
            for (int time: times) {temp += (mid / time ;)}

            if (temp >= n) {
                right = mid-1;
                answer = mid;
            } else {
                left = mid+1;
            }
        }
        return answer;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution());
    }
}
