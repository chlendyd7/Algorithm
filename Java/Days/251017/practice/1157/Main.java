import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String inputWord = br.readLine().toUpperCase();
        int[] check = new int[26];
        for (int i=0; i<inputWord.length(); i++) {
            check[inputWord.charAt(i) - 'A'] ++;
        }

        char result = '?';
        boolean duplicate = false;
        int max = 0;
        for (int i=0; i<26; i++) {
            if (check[i] > max) {
                max = check[i];
                result = (char)('A' + i);
                duplicate = false;
            } else if (max == check[i]) {
                duplicate = true;
            }
        }
        System.out.println(duplicate ? "?" : result);
    }
}
