// https://school.programmers.co.kr/learn/courses/30/lessons/42748

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] list = new int[commands.length];
        
        for(int i=0; i<commands.length; i++) {
            int[] command = commands[i];
            int start = command[0];
            int end = command[1];
            int pick = command[2];
            System.out.println(start + "" + end + "" + pick);
            int[] sliced = Arrays.copyOfRange(array, start-1, end);
            Arrays.sort(sliced);
            
            list[i] = sliced[pick-1];
        }
        return list;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution());
    }
}
