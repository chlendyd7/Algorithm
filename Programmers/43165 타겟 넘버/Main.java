class Solution {
    int answer = 0;
    public int solution(int[] numbers, int target) {
        dfs(numbers, 0, target, 0);
        return answer;
    }
    
    private void dfs(int[] numbers, int i, int target, int result) {
        if (i==numbers.length) {
            if (result == target) {
                answer ++;
            }
            return;
        }
        
        dfs(numbers, i+1, target, result + numbers[i]);
        dfs(numbers, i+1, target, result - numbers[i]);

    }
    
    
}