import util.Judge;

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        // TODO: input.txt 참고해서 테스트 입력값 채우기
        int[] numlist = {};
        int n = 0;

        var answer = sol.solution(numlist, n);
        Judge.check(answer);
    }
}
