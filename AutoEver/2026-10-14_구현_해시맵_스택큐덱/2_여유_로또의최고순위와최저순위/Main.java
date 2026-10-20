// https://school.programmers.co.kr/learn/courses/30/lessons/77484
/*
 
 */
import java.util.*;

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {

        List<Integer> winList = Arrays.stream(win_nums)
                                    .boxed()
                                    .collect(Collectors.toList());
        int[] answer = {};
        return answer;
    }
}
public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution());
    }
}
