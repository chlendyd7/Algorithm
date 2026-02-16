import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class refactor {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);

        // 101*101 격자인데, 차분 배열은 끝 지점(i+1)을 마킹하므로 102까지 확보하는 게 안전합니다.
        int[][] diff = new int[102][102];

        for (int i = 0; i < N; i++) {
            String[] pos = br.readLine().split(" ");
            int x1 = Integer.parseInt(pos[0]);
            int y1 = Integer.parseInt(pos[1]);
            int x2 = Integer.parseInt(pos[2]);
            int y2 = Integer.parseInt(pos[3]);

            // 1. 2차원 차분 배열 마킹 (O(1))
            diff[x1][y1] += 1;
            diff[x1][y2 + 1] -= 1;
            diff[x2 + 1][y1] -= 1;
            diff[x2 + 1][y2 + 1] += 1;
        }

        int result = 0;
        for (int i=1; i<101; i++) {
            for (int j=1; j<=100; j++) {
                diff[i][j] += diff[i-1][j] + diff[i][j-1] - diff[i-1][j-1]

                if (diff[i][j] > M) {
                    result ++;
                }
            }
        }
        System.out.print(result);
    }
}
