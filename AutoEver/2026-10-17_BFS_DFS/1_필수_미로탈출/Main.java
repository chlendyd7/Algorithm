// https://school.programmers.co.kr/learn/courses/30/lessons/159993
// 연습용: TODO 구현 전에는 실행 시 예외가 발생합니다.
import java.util.*;

class Solution {
    public int solution(String[] maps) {
        // TODO: S에서 시작해 L(레버)을 거쳐 E(출구)까지 가는 최소 시간. 불가능하면 -1.
        // X는 벽. 레버를 당기기 전에도 E 칸을 지나갈 수 있다. 같은 칸 재방문 가능.
        // BFS 두 번(S→L, L→E)으로 풀 수 있다. 첫 BFS에서 L을 못 찾으면 바로 -1.
        throw new UnsupportedOperationException("TODO: 레버 경유 BFS");
    }
}

public class Main {
    static void check(int expected, int actual) {
        if (expected != actual) throw new AssertionError("expected=" + expected + ", actual=" + actual);
        System.out.println("PASS " + actual);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        check(16, sol.solution(new String[]{"SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"}));
        check(-1, sol.solution(new String[]{"LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"}));
    }
}
