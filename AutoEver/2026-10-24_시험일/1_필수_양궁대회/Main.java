// https://school.programmers.co.kr/learn/courses/30/lessons/92342

class Solution {
    int[] info;
    int[] ryan = new int[11];
    int[] bestRyan = new int[11];
    int maxDiff = -1;
    
    
    public int[] solution(int n, int[] info) {
        this.info = info;
        dfs(0, n);
        if (maxDiff <= 0) {
            return new int[]{-1};
        }
        return bestRyan;
    }
    
    public void dfs(int idx, int arrowsLeft) {
        if (idx == 11) {
            ryan[10] += arrowsLeft;
            int diff = calculate();
            
            if (diff > maxDiff && diff > 0) {
                maxDiff = diff;
                bestRyan = ryan.clone();
            } else if (diff == maxDiff && diff > 0) {
                if (isBetter(ryan, bestRyan)) {
                    bestRyan = ryan.clone();
                }
            }
            ryan[10] -= arrowsLeft;
            return;
        }
        if (arrowsLeft > info[idx]) {
            ryan[idx] = info[idx] + 1;
            dfs(idx+1, arrowsLeft - ryan[idx]);
            ryan[idx] = 0;
        }
        
        dfs(idx+1, arrowsLeft);
    }
    
   public int calculate() {
       int rScore = 0;
       int aScore = 0;
       
       for (int i=0; i<11; i++) {
           if (ryan[i] == 0 && info[i] == 0) continue;
           
           if (ryan[i] > info[i]) {
               rScore += (10-i);
           } else {
               aScore += (10-i);
           }
       }
       return rScore - aScore;
   }
    
    public boolean isBetter(int[] current, int[] best) {
        for (int i=10; i>=0; i--) {
            if (current[i] > best[i]) return true;
            if (current[i] < best[i]) return false;
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
