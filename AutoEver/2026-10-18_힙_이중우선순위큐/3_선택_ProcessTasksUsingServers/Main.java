// https://leetcode.com/problems/process-tasks-using-servers/
// 연습용: 예제 확인 틀만 제공. TODO 구현 전 실행하면 예외가 발생합니다.
import java.util.*;

class Solution {
    public int[] assignTasks(int[] servers, int[] tasks) {
        // TODO: answer[j] = j번 작업이 배정된 서버 번호(0-based).
        // - j초에 작업 j가 큐에 들어온다.
        // - 빈 서버 중 무게 최소(같으면 번호 최소)에 배정. 빈 서버가 없으면 가장 빨리 끝나는 시각까지 기다린다.
        // - 종료 시각 <= 현재 시각인 서버는 다시 빈 서버로 본다.
        // - 종료 시각은 long (최대 약 4*10^10).
        throw new UnsupportedOperationException("TODO: 빈 서버 힙 + 사용 중 서버 힙");
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
        // 원문 예제
        check(new int[]{2, 2, 0, 2, 1, 2},
                sol.assignTasks(new int[]{3, 3, 2}, new int[]{1, 2, 3, 2, 1, 2}));
        check(new int[]{1, 4, 1, 4, 1, 3, 2},
                sol.assignTasks(new int[]{5, 1, 4, 3, 2}, new int[]{2, 1, 2, 4, 5, 2, 1}));
        // 자체 예제: 종료 시각 = 다음 작업 시각이면 바로 재사용
        check(new int[]{0, 0, 0, 0},
                sol.assignTasks(new int[]{1, 1}, new int[]{1, 1, 1, 1}));
        // 자체 예제: 서버가 없어 대기, 동시에 두 서버가 비면 무게 작은 서버 우선
        check(new int[]{1, 0, 1, 1},
                sol.assignTasks(new int[]{2, 1}, new int[]{5, 5, 1, 1}));
        // 서버 1대 경계
        check(new int[]{0, 0, 0},
                sol.assignTasks(new int[]{1}, new int[]{3, 3, 3}));
        // 대용량: 서버 1대에 작업 20만 개(각 20만초) -> 종료 시각이 int 범위를 넘는다. 시간 초과/예외 없이 끝나야 한다.
        int[] bigTasks = new int[200_000];
        Arrays.fill(bigTasks, 200_000);
        int[] bigAnswer = sol.assignTasks(new int[]{1}, bigTasks);
        check(new int[]{0}, new int[]{bigAnswer[bigAnswer.length - 1]});
    }
}
