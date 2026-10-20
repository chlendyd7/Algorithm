// https://school.programmers.co.kr/learn/courses/30/lessons/42885

import java.util.*;
/*
    sort해서 맨 앞하고 맨 뒤 비교,
    가능하면 둘 다 pop 안되면 맨 뒤만 pop 하면 되지 않나?
*/
class Solution {
    public int solution(int[] people, int limit) {
        // Deque<Integer> q = new LinkedList<>(people); 이거 못함?
        Arrays.sort(people);
        int left = 0;
        int right = people.length-1;
        int answer = 0;
        
        while (left <= right) {
            answer++;
            if (people[left] + people[right] <= limit) {
                left++;
                right--;
            } else {
                right --;
                
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
