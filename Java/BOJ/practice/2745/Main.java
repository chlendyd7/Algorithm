import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        String N = input[0];
        int B = Integer.parseInt(input[1]);

        long result = 0;
        int power = 1;

        for (int i=N.length()-1; i>=0; i--) {
            char ch = N.charAt(i);
            int value = 0;

            if(ch>= '0' && ch <= '9') {
                value = ch - '0';
            }
            else {
                value = ch - 'A' + 10;
            }

            result += value * power;

            power *= B;
        }
        System.out.println(result);
    }
}