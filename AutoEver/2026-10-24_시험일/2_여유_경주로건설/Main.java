// https://school.programmers.co.kr/learn/courses/30/lessons/67259
// 연습용: TODO 구현 전에는 실행 시 예외가 발생합니다.
import java.util.*;

class Solution {
    public int solution(int[][] board) {
        // TODO: N x N 격자(0=빈 칸, 1=벽). (0,0)에서 (N-1,N-1)까지 상하좌우로 도로를 건설.
        // 직선 도로 한 칸 = 100, 코너(직전 이동 방향과 다른 방향으로 꺾음) 한 번 = 500 추가.
        // 출발 칸에서 처음 이동할 때는 코너 비용이 없다. 최소 건설 비용을 반환.
        // 상태 = (행, 열, 도착 방향). 다익스트라(우선순위 큐) 또는 방향별 최소 비용 배열 + BFS 갱신.
        // 같은 칸이라도 도착 방향이 다르면 다른 상태다. dist[행][열][방향]으로 관리.
        throw new UnsupportedOperationException("TODO: 방향 상태 다익스트라");
    }
}

public class Main {
    static void check(int expected, int actual) {
        if (expected != actual) throw new AssertionError("expected=" + expected + ", actual=" + actual);
        System.out.println("PASS " + actual);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        check(900, sol.solution(new int[][]{{0, 0, 0}, {0, 0, 0}, {0, 0, 0}}));
        check(3800, sol.solution(new int[][]{
                {0, 0, 0, 0, 0, 0, 0, 1}, {0, 0, 0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 1, 0, 0}, {0, 0, 0, 0, 1, 0, 0, 0},
                {0, 0, 0, 1, 0, 0, 0, 1}, {0, 0, 1, 0, 0, 0, 1, 0}, {0, 1, 0, 0, 0, 1, 0, 0}, {1, 0, 0, 0, 0, 0, 0, 0}}));
        check(2100, sol.solution(new int[][]{{0, 0, 1, 0}, {0, 0, 0, 0}, {0, 1, 0, 1}, {1, 0, 0, 0}}));
        check(3200, sol.solution(new int[][]{
                {0, 0, 0, 0, 0, 0}, {0, 1, 1, 1, 1, 0}, {0, 0, 1, 0, 0, 0},
                {1, 0, 0, 1, 0, 1}, {0, 1, 0, 0, 0, 1}, {0, 0, 0, 0, 0, 0}}));
    }
}
