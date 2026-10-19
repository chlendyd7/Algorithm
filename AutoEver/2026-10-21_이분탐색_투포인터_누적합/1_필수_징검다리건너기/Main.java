// https://school.programmers.co.kr/learn/courses/30/lessons/64062
// 연습용: TODO 구현 전에는 실행 시 예외가 발생합니다.
import java.util.*;

class Solution {
    public int solution(int[] stones, int k) {
        // TODO: stones[i]는 i번째 징검다리를 밟을 수 있는 남은 횟수. 한 명이 건널 때마다 모든 돌이 1씩 줄고, 0이 된 돌은 못 밟는다.
        // 한 번에 최대 k칸까지 뛸 수 있다. 연속으로 k개 이상 0이면 못 건넌다. 건널 수 있는 최대 인원을 반환.
        // 파라메트릭 서치: n번째 사람이 건널 수 있는지 판정 = stones[i] < n 인 돌이 연속 k개 이상이면 불가능(n번째 사람은 stones[i] >= n 인 돌만 밟는다).
        // 이분탐색 범위는 1 ~ stones 최댓값(최대 2억). 판정은 O(N), 전체 O(N log M).
        throw new UnsupportedOperationException("TODO: 인원수 이분탐색 + 연속 구간 판정");
    }
}

public class Main {
    static void check(int expected, int actual) {
        if (expected != actual) throw new AssertionError("expected=" + expected + ", actual=" + actual);
        System.out.println("PASS " + actual);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        check(3, sol.solution(new int[]{2, 4, 5, 3, 2, 1, 4, 2, 5, 1}, 3));
        check(1, sol.solution(new int[]{1, 1, 1}, 3));
        check(5, sol.solution(new int[]{5, 1, 5, 1, 5}, 2));
        check(7, sol.solution(new int[]{7}, 1));
    }
}
