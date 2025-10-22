import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine().toUpperCase();
        int[] check = new int[26];
        int N = input.length();

        for (int i=0; i<N; i++) {
            int idx = input.charAt(i) - 'A';
            check[idx] ++;
        }

        int max = 0;
        boolean many = false;
        char word = '?';
        for (int i=0; i<N; i++) {
            int count = check[i];
            if (max < count) {
                max = count;
                word = (char)('A'+i);
                many = false;
            } else if (count == max) {
                many = true;
            }
        }
        System.out.println(many ? '?' : word);
    }
}