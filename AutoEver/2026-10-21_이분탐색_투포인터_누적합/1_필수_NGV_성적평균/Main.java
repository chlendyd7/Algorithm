// https://exam.hyundai-ngv.com/practice/6294
// 연습용: 입력/출력 틀만 제공. TODO 구현 전 실행하면 예외가 발생합니다.
import java.io.*;
import java.util.*;

public class Main {
    static double[] averages(int[] grades, int[][] queries) {
        // TODO: grades는 0-based 배열, queries의 A와 B는 원문처럼 1-based입니다.
        throw new UnsupportedOperationException("TODO: 성적 평균");
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
        int k = in.nextInt();
        int[] grades = new int[n];
        for (int i = 0; i < n; i++) grades[i] = in.nextInt();
        int[][] queries = new int[k][2];
        for (int i = 0; i < k; i++) {
            queries[i][0] = in.nextInt();
            queries[i][1] = in.nextInt();
        }
        double[] result = averages(grades, queries);
        StringBuilder out = new StringBuilder();
        for (double value : result) {
            out.append(String.format(Locale.US, "%.2f%n", value));
        }
        System.out.print(out);
    }
}

