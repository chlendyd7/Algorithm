// https://school.programmers.co.kr/learn/courses/30/lessons/42862

import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int[] check = new int[n + 2];
        
        for (int num : lost) {
            check[num]--;
        }
        for (int num : reserve) {
            check[num]++;
        }
        
        for (int i = 1; i <= n; i++) {
            if (check[i] < 0) { // 체육복이 없는 학생인 경우
                if (check[i - 1] > 0) {
                    check[i - 1]--;
                    check[i]++;
                } else if (check[i + 1] > 0) {
                    check[i + 1]--;
                    check[i]++;
                }
            }
        }
        
        int answer = n;
        for (int i = 1; i <= n; i++) {
            if (check[i] < 0) {
                answer--; // 끝내 체육복을 구하지 못한 학생 수만큼 차감
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
