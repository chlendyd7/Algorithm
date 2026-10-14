import util.Judge;

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        int[] numlist = {1, 2, 3};
        int n = 1;

        var answer = sol.solution(numlist, n);
        Judge.check(answer);
    }
}
