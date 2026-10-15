// https://school.programmers.co.kr/learn/courses/30/lessons/42747

class Solution {
    // TODO: 파라미터/리턴타입 문제에 맞게 채우기
    public int solution() {
        Arrays.sort(citations);
        int n = citations.length;
        int hIndex = 0;
        for (int i=0; i<n; i++) {
            
            if(citations[i] >= n-i) {
                hIndex = n-i;
                break;
            }
        }
            
        return hIndex;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution());
    }
}
