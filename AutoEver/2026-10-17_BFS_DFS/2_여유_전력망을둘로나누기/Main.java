// https://school.programmers.co.kr/learn/courses/30/lessons/86971
// 연습용: TODO 구현 전에는 실행 시 예외가 발생합니다.
import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        // TODO: wires는 n개 노드 트리의 간선 n-1개(1-based). 간선 하나를 끊어 두 네트워크로 나눌 때
        // 두 네트워크 노드 수 차이의 절댓값 최솟값 반환. n<=100이므로 간선을 하나씩 빼고 한쪽 연결요소 크기를 센다.
        throw new UnsupportedOperationException("TODO: 간선 하나씩 제거 + 연결요소 크기");
    }
}

public class Main {
    static void check(int expected, int actual) {
        if (expected != actual) throw new AssertionError("expected=" + expected + ", actual=" + actual);
        System.out.println("PASS " + actual);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        check(3, sol.solution(9, new int[][]{{1,3}, {2,3}, {3,4}, {4,5}, {4,6}, {4,7}, {7,8}, {7,9}}));
        check(0, sol.solution(4, new int[][]{{1,2}, {2,3}, {3,4}}));
        check(1, sol.solution(7, new int[][]{{1,2}, {2,7}, {3,7}, {3,4}, {4,5}, {6,7}}));
    }
}
