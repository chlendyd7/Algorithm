// https://school.programmers.co.kr/learn/courses/30/lessons/42839

class Solution {
    // TODO: 파라미터/리턴타입 문제에 맞게 채우기
    Set<Integer> numberSet = new HashSet<>();
    
    public int solution(String numbers) {
        boolean[] visited = new boolean[numbers.length()];
        findNumbers("", visited, numbers);
        
        int answer = 0;
        for (int num: numberSet) {
            if (isPrime(num)) {
                answer++;
            }
        }
        
        return answer;
    }
    
    public void findNumbers(String current, boolean[] visited, String numbers) {
        if (!current.isEmpty()) {
            numberSet.add(Integer.parseInt(current));
        }
        
        for (int i=0; i< numbers.length(); i++) {
            if (!visited[i]) {
                visited[i] = true;
                findNumbers(current + numbers.charAt(i), visited, numbers);
                visited[i] = false;
            }
        }
    }
    
    public boolean isPrime(int num) {
        if (num < 2) return false;
        for (int i=2; i*i<=num; i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution());
    }
}
