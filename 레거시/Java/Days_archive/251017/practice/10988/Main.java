import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String word = br.readLine();
        int N = word.length();
        boolean check = false;
        for (int i=0; i<N/2; i++) {
            if (word.charAt(i) != word.charAt(N - i-1)) {
                System.out.println(0);
                check = true;
                break;
            }
        }
        if (!check) System.out.println(1);
    }
}