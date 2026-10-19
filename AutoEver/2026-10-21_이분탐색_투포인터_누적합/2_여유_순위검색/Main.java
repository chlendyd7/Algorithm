// https://school.programmers.co.kr/learn/courses/30/lessons/72412
// 연습용: TODO 구현 전에는 실행 시 예외가 발생합니다.
import java.util.*;

class Solution {
    public int[] solution(String[] info, String[] query) {
        // TODO: info는 "언어 직군 경력 소울푸드 점수", query는 "언어 and 직군 and 경력 and 소울푸드 점수" ("-"는 무관).
        // 각 query에 맞고 점수가 기준 이상인 지원자 수를 순서대로 반환.
        // 목표: info<=50,000, query<=100,000. query마다 info 전체를 훑으면 시간 초과.
        // 방향: 지원자 1명당 조건 조합(각 항목 값 또는 "-", 16개)을 키로 HashMap<String, List<Integer>>에 점수 저장
        //       → 키별 점수 정렬 → query마다 lower bound(이분탐색).
        throw new UnsupportedOperationException("TODO: 해시 + 이분탐색");
    }
}

public class Main {
    static void check(int[] expected, int[] actual) {
        if (!Arrays.equals(expected, actual)) {
            throw new AssertionError("expected=" + Arrays.toString(expected) + ", actual=" + Arrays.toString(actual));
        }
        System.out.println("PASS " + Arrays.toString(actual));
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        String[] info = {
            "java backend junior pizza 150", "python frontend senior chicken 210",
            "python frontend senior chicken 150", "cpp backend senior pizza 260",
            "java backend junior chicken 80", "python backend senior chicken 50"};
        String[] query = {
            "java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
            "cpp and - and senior and pizza 250", "- and backend and senior and - 150",
            "- and - and - and chicken 100", "- and - and - and - 150"};
        check(new int[]{1, 1, 1, 1, 2, 4}, sol.solution(info, query));
    }
}
