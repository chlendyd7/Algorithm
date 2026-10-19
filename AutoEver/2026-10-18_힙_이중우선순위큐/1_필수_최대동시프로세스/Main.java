// 자체 문제: 지난 시험 "start/end 입력 → 필요한 프로세스 최대 개수" 재현. 온라인 judge 없음.
// 같은 구조의 원문: 프로그래머스 호텔 대실 (gap=10, 시각은 분 단위로 변환)
// 연습용: TODO 구현 전에는 실행 시 예외가 발생합니다.
import java.util.*;

public class Main {
    // tasks[i] = {start, end}, start < end. 한 프로세서는 이전 end + gap <= 다음 start 일 때만 재사용 가능.
    // 모든 작업을 처리하는 데 필요한 최소 프로세서 수를 반환. 입력은 정렬돼 있지 않다.

    static int minProcessorsHeap(int[][] tasks, int gap) {
        // TODO 풀이 1: start 정렬 + 종료 시각 최소 힙.
        throw new UnsupportedOperationException("TODO: 힙 풀이");
    }

    static int minProcessorsSweep(int[][] tasks, int gap) {
        // TODO 풀이 2: 힙 없이. 이벤트 스위핑 또는 start 배열/end 배열을 각각 정렬해 투포인터.
        throw new UnsupportedOperationException("TODO: 스위핑 풀이");
    }

    static void check(int expected, int[][] tasks, int gap) {
        int heap = minProcessorsHeap(tasks, gap);
        int sweep = minProcessorsSweep(tasks, gap);
        if (heap != expected || sweep != expected) {
            throw new AssertionError("expected=" + expected + ", heap=" + heap + ", sweep=" + sweep);
        }
        System.out.println("PASS " + expected);
    }

    public static void main(String[] args) {
        // gap=0: 끝나는 시각에 바로 다음 작업 시작 가능
        check(2, new int[][]{{1,3}, {2,4}, {3,5}}, 0);
        check(1, new int[][]{{1,2}, {2,3}, {3,4}}, 0);
        // gap=1: 끝난 다음 시각부터 재사용 (end < start)
        check(3, new int[][]{{1,3}, {2,4}, {3,5}}, 1);
        check(2, new int[][]{{1,2}, {2,3}, {3,4}}, 1);
        // 입력이 start 순이 아님
        check(2, new int[][]{{5,7}, {1,6}, {2,3}}, 0);
        // 호텔 대실 예제 (분 단위, gap=10)
        check(3, new int[][]{{900,1020}, {1000,1100}, {860,920}, {850,1160}, {1100,1280}}, 10);
        check(1, new int[][]{{550,610}, {620,740}}, 10);
        check(3, new int[][]{{620,750}, {620,750}, {620,750}}, 10);
        // 작업 1개
        check(1, new int[][]{{5,6}}, 100);
        // end + gap 이 int 범위를 넘음: 오버플로하면 재사용으로 오판
        check(2, new int[][]{{1,1_500_000_000}, {2,1_500_000_001}}, 1_000_000_000);
    }
}
