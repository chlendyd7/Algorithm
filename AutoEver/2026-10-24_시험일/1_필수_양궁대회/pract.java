/*
1. 딱 한발만 더 어피치보다 맞추면 됨
2. 먹을건지 말지만 판단해서 진행

*/
import java.util.*;

class Solution {
    int maxValue;
    int[] maxArray;
        
    public int[] solution(int n, int[] info) {
        int[] me = new int[info.length];
        
        maxValue = 0;
        maxArray = new int[info.length];
        
        dfs(0, n, info, me);
        System.out.println(maxValue);
        System.out.println(Arrays.toString(maxArray));
        return maxValue > 0 ? maxArray : new int[]{-1};
    }
    
    public void dfs(int depth, int arrows, int[] info, int[] me) {
        if (depth == 10 || arrows == 0) {
            int[] copy = Arrays.copyOf(me, me.length);
            copy[10] += arrows;
            calculate(info, copy);
            return;
        }

        //쏜다
        if (info[depth] < arrows) {
            int[] copy = Arrays.copyOf(me, me.length);
            int shot = info[depth] + 1;
            copy[depth] = shot;
            dfs(depth+1, arrows-shot, info, copy);
        }
        dfs(depth+1, arrows, info, me);
    }
    

    public void calculate(int[] info, int[] me) {
        int check = 0;
        
        for (int i=0; i<info.length; i++) {
            if (me[i] > info[i]) {
                check += 10-i;
            } else if (info[i] > 0) {
                check -= 10 -i;
            }
        }
        if (check <= 0) return;

        if (maxValue < check) {
            maxValue = check;
            maxArray = Arrays.copyOf(me, me.length);
            return;
        }

        if (maxValue == check) {
            for (int i=10; i >= 0; i--) {
                if (me[i] == 0 && maxArray[i] == 0) continue;
                if (me[i] > maxArray[i]) {
                    maxArray = Arrays.copyOf(me, me.length);
                }
                    return;
                };
            }
        
        return;
    }
}