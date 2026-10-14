// Python: input(), int(input()), list(map(int, input().split())) 로 끝
// Java: Scanner는 느려서 SWEA/Codeforces/AtCoder처럼 입력 큰 문제에선 시간초과 남
//       → BufferedReader + StringTokenizer 조합을 기본으로 쓰는 게 안전함
// (프로그래머스는 입출력 직접 안 하고 solution() 파라미터로 받아서 이 파일은 SWEA/CF/AtCoder용)

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 실제 제출 코드에서는 이렇게 System.in에서 직접 읽음:
        // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // int n = Integer.parseInt(br.readLine());
        // StringTokenizer st = new StringTokenizer(br.readLine());
        // int a = Integer.parseInt(st.nextToken());

        // ── 연습 1: 입력 파싱 (여기선 System.in 대신 배열로 흉내냄) ──
        // "3\n1 2 3" 같은 입력이 온다고 가정. 첫 줄 = 개수, 둘째 줄 = 공백으로 구분된 숫자들.
        // Python: n = int(input()); nums = list(map(int, input().split()))
        String[] lines = {"3", "1 2 3"};

        int n = Integer.parseInt(lines[0]); // 문자열 "3" -> 숫자 3

        // StringTokenizer: 공백 기준으로 문자열을 토큰(조각)으로 쪼개주는 도구
        // Python의 "1 2 3".split() 이랑 같은 역할
        StringTokenizer st = new StringTokenizer(lines[1]);
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken()); // 토큰 하나 꺼내서(String) 숫자로 변환
        }
        System.out.println(Arrays.toString(nums)); // [1, 2, 3]

        // ── 출력: 모아서 한 번에 ──────────────────────────────
        // println을 반복문 안에서 여러 번 호출하면 매번 시스템 호출이 발생해서 느림.
        // StringBuilder에 다 모았다가 마지막에 한 번만 출력하는 게 안전.
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 3; i++) {
            sb.append(i).append('\n');
        }
        System.out.print(sb);

        // ── 연습 2: Scanner와 비교 ────────────────────────────
        // Scanner sc = new Scanner(System.in);
        // int x = sc.nextInt(); // 숫자 하나 바로 읽기 — 코드는 짧지만 내부적으로 매번 파싱/버퍼 처리가 무거움
        //
        // BufferedReader는 "한 줄 전체를 통째로" 빠르게 읽어온 다음 StringTokenizer로 잘라 쓰는 구조라
        // 입력 줄 수가 많은 SWEA/Codeforces/AtCoder 문제에서 Scanner 쓰면 시간초과 나는 경우가 많음.
        // → 기본은 BufferedReader, 입력이 몇 줄 안 되는 간단한 문제면 Scanner도 무방.
    }
}
