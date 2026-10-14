// Python: input(), int(input()), list(map(int, input().split())) 로 끝
// Java: Scanner는 느려서 SWEA/Codeforces/AtCoder처럼 입력 큰 문제에선 시간초과 남
//       → BufferedReader + StringTokenizer 조합을 기본으로 쓰는 게 안전함
// (프로그래머스는 입출력 직접 안 하고 solution() 파라미터로 받아서 이 파일은 SWEA/CF/AtCoder용)

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 예시: 한 줄에 숫자 하나
        // int n = Integer.parseInt(br.readLine());

        // 예시: 한 줄에 숫자 여러 개, 공백으로 구분 — Python의 list(map(int, input().split()))에 대응
        // StringTokenizer st = new StringTokenizer(br.readLine());
        // int a = Integer.parseInt(st.nextToken());
        // int b = Integer.parseInt(st.nextToken());

        // TODO 1: 테스트용으로 String[] lines = {"3", "1 2 3"} 를 입력이라 치고
        // (실제 System.in 대신 이 배열로 연습)
        // 첫 줄 n=3 파싱하고, 둘째 줄 "1 2 3"을 StringTokenizer로 쪼개서 int 배열로 만들어 출력해보기.
        String[] lines = {"3", "1 2 3"};
        int n = Integer.parseInt(lines[0]);
        StringTokenizer st = new StringTokenizer(lines[1]);
        int[] nums = new int[n];
        // 여기서부터 작성: nums[i] = Integer.parseInt(st.nextToken()) 반복


        // 예시: 출력 — println 여러 번 하면 느림, 한꺼번에 모아서 출력하는 게 안전
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 3; i++) {
            sb.append(i).append('\n');
        }
        System.out.print(sb);

        // TODO 2: Scanner로도 똑같이 한 줄 입력 받는 코드 작성해보고
        // (Scanner sc = new Scanner(System.in); sc.nextInt();)
        // 왜 코테에서 BufferedReader를 더 권장하는지 생각해보기 (속도 차이)

    }
}
