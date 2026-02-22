import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);

        List<Integer> gems = new ArrayList<>();
        int left = 1;
        int right = 0;

        for (int i=0;i<M;i++) {
            int currentGem = Integer.parseInt(br.readLine());
            gems.add(currentGem);

            right = Math.max(right, currentGem);
        }
        int zilous = right;
        while (left <= right) {
            int mid = (left + right) / 2;
            int totalCount = 0;
            for (int i=0; i<M;i++) {
                totalCount += (gems.get(i) / mid);
                if (gems.get(i) % zilous != 0) totalCount += 1;
            }

            if (totalCount <= N) {
                zilous = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        System.out.println(zilous);
    }
}