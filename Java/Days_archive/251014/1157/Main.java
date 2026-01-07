import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String inputs = br.readLine().toUpperCase();
        int [] count = new int[26];

        for (int i=0; i<inputs.length(); i++) {
            char word = inputs.charAt(i);
            count[word - 'A'] ++;
        }

        int max=-1;
        char answer = '?';
        boolean duplicate = false;

        for (int i=0; i<26; i++) {
            if(count[i] > max) {
                max = count[i];
                answer = (char)(i+'A');
                duplicate = false;
            } else if (count[i] == max) {
                duplicate = true;
            }
        }
        //조건식 a:b
        System.out.println(duplicate ? '?' : answer);
    }
}
