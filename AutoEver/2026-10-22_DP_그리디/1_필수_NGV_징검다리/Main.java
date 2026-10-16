// https://exam.hyundai-ngv.com/practice/6293
// 연습용: 입력/출력 틀만 제공. TODO 구현 전 실행하면 예외가 발생합니다.
import java.io.*;
import java.util.*;

public class Main {
    static int lengthOfLIS(int[] heights) {
        // TODO: 입력 순서를 유지하며 높이가 엄격히 증가하는 부분 수열의 최대 길이.
        throw new UnsupportedOperationException("TODO: 징검다리 LIS");
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
        int[] heights = new int[n];
        for (int i = 0; i < n; i++) heights[i] = in.nextInt();
        System.out.println(lengthOfLIS(heights));
    }
}

