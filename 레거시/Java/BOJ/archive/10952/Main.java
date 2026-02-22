import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String line = br.readLine();

            String [] nums = line.split(" ");

            int A = Integer.parseInt(nums[0]);
            int B = Integer.parseInt(nums[1]);

            if (A == 0 && B == 0) {
                break;
            }

            int sum = A + B;
            System.out.println(sum);
        }
    }    
}
