// https://school.programmers.co.kr/learn/courses/30/lessons/42586
import java.util.*;

class Solution {
    public int solution() {
        Queue<Integer> queue = new LinkedList<>();
        
        for (int i=0; i<progresses.length; i++) {
            int workDay = (100 - progresses[i]) / speeds[i];
            if ((100 - progresses[i]) % speeds[i] != 0) {
                workDay += 1;
            }
            queue.add(workDay);
        }

        List<Integer> answerList = new ArrayList<>();
        
        while (!queue.isEmpty()) {
            int currentDay = queue.poll();
            int count = 1;

            while (!queue.isEmty() && queue.peek() <= currentDay) {
                queue.poll();
                count++;
            }
            answerList.add(count);
        }

        return answerList.stream().mapToInt(i -> i).toArray();
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution());
    }
}
