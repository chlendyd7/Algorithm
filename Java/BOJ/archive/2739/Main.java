import java.io.*;
import java.util.*;

// 구구단
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int X = Integer.parseInt(br.readLine());
        int N = Integer.parseInt(br.readLine());
        int totalAmount = 0;

        for (int i = 0; i < N; i++) {
            String[] numbers = br.readLine().split(" ");

            int a = Integer.parseInt(numbers[0]);
            int b = Integer.parseInt(numbers[1]);

            totalAmount += (a * b);
        }

        if (X == totalAmount) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}