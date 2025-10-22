import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int X = Integer.parseInt(br.readLine()); // 테스트 케이스 수
        int N = Integer.parseInt(br.readLine());
        int result = 0;
        for (int i = 0; i < N; i ++) {
            String [] nums = br.readLine().split(" ");
            int a = Integer.parseInt(nums[0]);
            int b = Integer.parseInt(nums[1]);
            result += (a * b);
        }

        if (result == X) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}