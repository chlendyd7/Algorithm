// https://exam.hyundai-ngv.com/practice/11001

import java.io.*;
import java.util.*;

public class Main {

    static class Number {
        String original;
        int x;
        int y;

        Number(String original) {
            this.original = original;

            int dotIndex = original.indexOf('.');

            if (dotIndex == -1) {
                // 소수점이 없는 경우
                x = Integer.parseInt(original);
                y = -1;
            } else {
                // 소수점 앞부분
                x = Integer.parseInt(
                        original.substring(0, dotIndex)
                );

                // 소수점 뒷부분
                y = Integer.parseInt(
                        original.substring(dotIndex + 1)
                );
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br =
                new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine().trim());
        Number[] numbers = new Number[n];

        for (int i = 0; i < n; i++) {
            numbers[i] = new Number(br.readLine().trim());
        }

        Arrays.sort(numbers, (a, b) -> {
            if (a.x != b.x) {
                return Integer.compare(a.x, b.x);
            }

            return Integer.compare(a.y, b.y);
        });

        StringBuilder sb = new StringBuilder();

        for (Number number : numbers) {
            sb.append(number.original).append('\n');
        }

        System.out.print(sb);
    }
}
