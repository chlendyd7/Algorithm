import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int [] nums = Arrays.stream(br.readLine().split(" "))
                        .mapToInt(Integer::parseInt).toArray();
        int V = Integer.parseInt(br.readLine());
        int count = 0;
        for (int i = 0 ; i < N; i ++) {
            if (nums[i] == V) {
                count ++;
            }
        }
        System.out.println(count);
    }
}
