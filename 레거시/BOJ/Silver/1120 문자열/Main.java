import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // StringTokenizer는 split보다 빠르고 공백 처리가 깔끔합니다.
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        String a = st.nextToken();
        String b = st.nextToken();
        
        // 최소 차이값은 최대 문자열 A의 길이를 넘을 수 없습니다.
        int minDiff = a.length();

        // 탐색 범위를 b.length() - a.length()까지 설정
        for (int i = 0; i <= b.length() - a.length(); i++) {
            int currentDiff = 0;
            for (int j = 0; j < a.length(); j++) {
                if (a.charAt(j) != b.charAt(i + j)) {
                    currentDiff++;
                }
                // 만약 계산 중에 이미 minDiff보다 커지면 더 볼 필요가 없습니다 (Pruning)
                if (currentDiff >= minDiff) break;
            }
            minDiff = Math.min(minDiff, currentDiff);
        }

        System.out.println(minDiff);
    }
}