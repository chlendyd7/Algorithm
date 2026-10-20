// https://school.programmers.co.kr/learn/courses/30/lessons/43165

import java.util.*;

class Solution {
    int[] globalNumbers;
    int globalTarget;
    int answer = 0;
    
    public int solution(int[] numbers, int target) {
        globalNumbers = numbers;
        globalTarget = target;
        dfs(0,0);
        return answer;
    }
    
    public void dfs(int result, int idx) {
        if (idx == globalNumbers.length) {
            if (result == globalTarget) {
                answer+=1;
            }
            return;
        }
        dfs(result + globalNumbers[idx], idx+1);
        dfs(result - globalNumbers[idx], idx+1);
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution());
    }
}
