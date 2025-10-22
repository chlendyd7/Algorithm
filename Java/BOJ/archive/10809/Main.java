import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        int[] result = new int[26];
        Arrays.fill(result, -1);

        for (int i =0; i <s.length(); i++) {
            char ch = s.charAt(i);
            int index = ch - 'a';

            if (result[index] == -1) {
                result[index] = i;
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int value : result) {
            sb.append(value).append(" ");
        }

        System.out.println(sb.toString().trim());
    }    
}
