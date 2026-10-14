// https://school.programmers.co.kr/learn/courses/30/lessons/120861

class Solution {
    // TODO: 파라미터/리턴타입 문제에 맞게 채우기
    import java.util.*;

class Solution {
    public int[] solution(String[] keyinput, int[] board) {
        HashMap<String, int[]> moveMap = new HashMap<>();
        moveMap.put("up", new int[]{0, 1});
        moveMap.put("down", new int[]{0, -1});
        moveMap.put("left", new int[]{-1, 0});
        moveMap.put("right", new int[]{1, 0});
        
        
        int limitX = board[0]/2;
        int limitY = board[1]/2;
        
        int x = 0;
        int y = 0;
        
        for (String key: keyinput) {
            int[] move = moveMap.get(key);
            
            int nextX = x + move[0];
            int nextY = y + move[1];
            
            if (nextX >= -limitX && nextX <= limitX && nextY >= -limitY && nextY <= limitY ) {
                x = nextX;
                y = nextY;
            }
            
        }
        
        return new int[]{x, y};
    }
}
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution());
    }
}
