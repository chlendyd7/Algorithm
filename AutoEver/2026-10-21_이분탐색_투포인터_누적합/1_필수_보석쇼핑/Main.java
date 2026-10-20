// https://school.programmers.co.kr/learn/courses/30/lessons/67258
// 연습용: TODO를 구현하기 전에는 예제 실행 시 예외가 발생합니다.
import java.util.*;

class Solution {
    public int[] solution(String[] gems) {
        int kinds = new HashSet<>(Arrays.asList(gems)).size();
        Map<String, Integer> cnt = new HashMap<>();

        int best = Integer.MAX_VALUE, bs = 0, be = 0;
        int left = 0;
        for (int right = 0; right < gems.length; right++) {
            cnt.merge(gems[right], 1, Integer::sum);

            while(cnt.size() == kinds) {
                if (right - left < best) { best = right - left; bs=left; be=right;}

                String g = gems[left];
                if (cnt.merge(g, -1, Integer::sum) == 0) cnt.remove(g);
                left++;
            }
        }
        return new int[] {bs+1, be+1};
    }
}

public class Main {
    static void check(int[] expected, int[] actual) {
        if (!Arrays.equals(expected, actual)) {
            throw new AssertionError("expected=" + Arrays.toString(expected)
                + ", actual=" + Arrays.toString(actual));
        }
        System.out.println("PASS " + Arrays.toString(actual));
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        check(new int[]{3, 7}, sol.solution(new String[]{
            "DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"}));
        check(new int[]{1, 3}, sol.solution(new String[]{"AA", "AB", "AC", "AA", "AC"}));
        check(new int[]{1, 1}, sol.solution(new String[]{"XYZ", "XYZ", "XYZ"}));
        check(new int[]{1, 5}, sol.solution(new String[]{"ZZZ", "YYY", "NNNN", "YYY", "BBB"}));
    }
}

