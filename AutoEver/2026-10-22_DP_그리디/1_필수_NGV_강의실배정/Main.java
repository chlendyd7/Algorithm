// https://exam.hyundai-ngv.com/practice/6291
// 연습용: 입력/출력 틀만 제공. TODO 구현 전 실행하면 예외가 발생합니다.
import java.io.*;
import java.util.*;

public class Main {
    static int maxLectures(int[][] lectures) {
        // TODO: 강의실은 1개. 종료 시간과 다음 시작 시간이 같아도 연속 배정 가능.
        throw new UnsupportedOperationException("TODO: 강의실 배정");
    }

    static class TokenReader {
        private final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        private StringTokenizer st;

        int nextInt() throws IOException {
            while (st == null || !st.hasMoreTokens()) {
                String line = br.readLine();
                if (line == null) throw new EOFException("입력이 부족합니다.");
                st = new StringTokenizer(line);
            }
            return Integer.parseInt(st.nextToken());
        }
    }

    public static void main(String[] args) throws Exception {
        TokenReader in = new TokenReader();
        int n = in.nextInt();
        int[][] lectures = new int[n][2];
        for (int i = 0; i < n; i++) {
            lectures[i][0] = in.nextInt();
            lectures[i][1] = in.nextInt();
        }
        System.out.println(maxLectures(lectures));
    }
}

