// https://school.programmers.co.kr/learn/courses/30/lessons/43163

import java.util.*;
/*
    한번에 한 개 변환 가능
    한 개만 다른지 확인, 변하고 안변하고
*/

class Solution {
    // int answer = Integer.MaxValue;
    int answer = Integer.MAX_VALUE;
    String target;
    String[] words;
    boolean[] visited;
    
    public int solution(String begin, String target, String[] words) {
        this.target = target;
        this.words = words;
        visited = new boolean[words.length];
        
        boolean hasTaget = false;
        for (String w: words) {
            if (w.equals(target)) {
                hasTaget = true;
                break;
            }
        }
        
        dfs(begin, 0);
        return answer==Integer.MAX_VALUE ? 0 : answer;
        
    }
    
    public void dfs(String now, int count) {
        if (now.equals(target)) {
            answer = Math.min(answer, count);
            return;
        }

        for (int i=0; i<words.length;i++) {
            if(!visited[i] && check(now, words[i])) {
                visited[i] = true;
                dfs(words[i], count+1);
                visited[i] = false;
            }
        }
    }   
     

    public boolean check(String str1, String str2) {
        String[] list1 = str1.split("");
        String[] list2 = str2.split("");
        int check = 0;
        for (int i=0; i<list1.length; i++) {
            if (!list1[i].equals(list2[i])) {
                check += 1;
            }
        }
        if (check == 1) {
            return true;
        }
        return false;
    }
}


public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution());
    }
}
