// https://school.programmers.co.kr/learn/courses/30/lessons/12909
// 내일 이거 물어보기

import java.util.*;
class Solution {
    boolean solution(String s) {
        Queue<String> q = new LinkedList<>();
        
        for (String c: s.split("")) {
            if (c.equals("(")) {
                q.add(c);
            } else {
                if (q.isEmpty()) {
                    return false;
                } else {
                    q.poll();
                }
            }
        }
        
        boolean answer = true;

        return answer;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution());
    }
}
