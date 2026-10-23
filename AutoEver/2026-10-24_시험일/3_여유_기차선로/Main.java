// 2025 카카오 하반기 2차, Lv3 "기차 선로" (프로그래머스)
// 연습용: TODO 구현 전에는 실행 시 예외가 발생합니다.
// n x m 격자(n*m <= 20). 칸: 0 빈칸, 1~7 선로 종류, -1 장애물. 선로 7종의 모양은 문제 페이지 그림 참고.
// 규칙: (1,1)의 1번 선로에서 기차가 오른쪽으로 출발, (n,m)에 도착, 놓인 모든 선로를 한 번 이상 지나감,
//       3번(#) 선로는 상하좌우 모두 연결되어야 함. 빈칸에 선로를 놓는(또는 비워 두는) 방법의 수를 반환(없으면 0).
// 그룹 #1(35%): 3번 선로 고려 불필요. 그룹 #2(65%): 제한 없음.
// 방법 A: 빈칸마다 {비움, 선로1~7} 후보를 백트래킹, 놓을 때마다 이웃 연결 일치 여부로 가지치기, 끝에서 기차를 시뮬레이션해 검증.
import java.util.*;

class Solution {
    public int solution(int[][] grid) {
        // TODO
        throw new UnsupportedOperationException("TODO");
    }
}

public class Main {
    static void check(String name, int expected, int actual) {
        if (expected != actual) throw new AssertionError(name + ": expected=" + expected + ", actual=" + actual);
        System.out.println("PASS " + name + " -> " + actual);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        // 프로그래머스 공식 예제 6개
        check("ex1", 2, sol.solution(new int[][]{{1, 0, -1}, {0, 0, 7}, {0, 0, 2}}));
        check("ex2", 2, sol.solution(new int[][]{{1, 0, 0, 0, 0, -1, -1}, {-1, 0, 0, 1, 0, 0, 1}}));
        check("ex3", 4, sol.solution(new int[][]{{1, 0, 0, 0, 0}, {0, 0, 3, 0, 2}, {0, 0, 0, 0, 2}}));
        check("ex4", 644, sol.solution(new int[][]{{1, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 1}}));
        check("ex5", 1, sol.solution(new int[][]{{1, 7}, {0, 2}}));
        check("ex6", 0, sol.solution(new int[][]{{1, -1, 0, 0}, {-1, 0, 0, 0}, {0, 0, 0, -1}, {0, 0, -1, 1}}));
    }
}
