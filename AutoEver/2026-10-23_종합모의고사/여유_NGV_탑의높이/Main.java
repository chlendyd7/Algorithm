//https://exam.hyundai-ngv.com/app/assessment/index.html?xid=501096&xsrfToken=FZWFKNAOqi2f2fWdHoXnF6DTeFQcvzyx&testType=practice

import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static long k;
    static long[] heights;
    static long[] prefix;

    public static void main(String[] args) throws IOException {
        BufferedReader br =
                new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Long.parseLong(st.nextToken());

        heights = new long[n];
        prefix = new long[n + 1];

        st = new StringTokenizer(br.readLine());

        long maxHeight = 0;

        for (int i = 0; i < n; i++) {
            heights[i] = Long.parseLong(st.nextToken());
            prefix[i + 1] = prefix[i] + heights[i];
            maxHeight = Math.max(maxHeight, heights[i]);
        }

        long low = maxHeight;

        // 안정적인 탑에서 최대 높이는 평균 높이 + (n - 1) 이하.
        // 최종 높이의 총합은 초기 총합 + k 이하.
        long high = (prefix[n] + k) / n + n - 1L;

        while (low < high) {
            long mid = low + (high - low + 1) / 2;

            if (canMake(mid)) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }

        System.out.println(low);
    }

    static boolean canMake(long target) {
        int left = 0;
        int right = 0; // 높일 오른쪽 구간의 끝 다음 인덱스

        for (int p = 0; p < n; p++) {
            // 왼쪽에서 높일 필요가 없는 칸을 건너뜀.
            // 높일 왼쪽 구간: [left, p]
            while (left <= p
                    && heights[left] - left >= target - p) {
                left++;
            }

            // 오른쪽 구간에는 중심 p를 포함하지 않음.
            if (right < p + 1) {
                right = p + 1;
            }

            // 높일 오른쪽 구간: [p + 1, right - 1]
            while (right < n
                    && heights[right] + right < target + p) {
                right++;
            }

            long cost = 0;

            // 왼쪽 + 중심 비용
            if (left <= p) {
                long count = p - left + 1L;

                // 각 칸의 필요 높이: target - p + i
                long requiredSum =
                        count * (target - p)
                        + indexSum(left, p);

                long currentSum =
                        prefix[p + 1] - prefix[left];

                cost += requiredSum - currentSum;
            }

            // 오른쪽 비용
            if (p + 1 < right) {
                long count = right - p - 1L;

                // 각 칸의 필요 높이: target + p - i
                long requiredSum =
                        count * (target + p)
                        - indexSum(p + 1, right - 1);

                long currentSum =
                        prefix[right] - prefix[p + 1];

                cost += requiredSum - currentSum;
            }

            if (cost <= k) {
                return true;
            }
        }

        return false;
    }

    // start + (start + 1) + ... + end
    static long indexSum(int start, int end) {
        return ((long) start + end) * (end - start + 1L) / 2;
    }
}
