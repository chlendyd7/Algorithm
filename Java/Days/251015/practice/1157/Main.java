import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] chars = new int[26];
        String inputs = br.readLine().toUpperCase();

        for (int i=0; i<inputs.length(); i++) {
            char word = inputs.charAt(i);
            chars[word - 'A']++;
        }

        int max = -1;
        char answer = '?';
        boolean duplicate = false;
        for (int i=0; i<26; i++) {
            if(chars[i] > max) {
                max = chars[i];
                answer = (char)(i+'A');
                duplicate = false;
            } else if (chars[i] == max) {
                duplicate = true;
            }
        }
        System.out.println(duplicate ? '?' : answer);
    }
}