import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int result = 0;
        for (int i=0; i<N; i++) {
            if (isChecker(br.readLine())) result ++;
        }
        System.out.println(result);
    }

    public static boolean isChecker(String input) {
        boolean[] check = new boolean[26];
        char prev = input.charAt(0);
        check[prev - 'a'] = true;
        for (int i=1; i<input.length(); i++) {
            if (prev != input.charAt(i)) {
                if (check[input.charAt(i) - 'a']) return false; // check가 이미 되있으면
                prev = input.charAt(i);
                check[prev - 'a'] = true;
            }
        }
        return true;
    }
}