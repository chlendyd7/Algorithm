import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int count = Integer.parseInt(br.readLine());
        int cnt = 0;
        for (int i=0; i<count; i++) {
            if (check(br.readLine())) {
                cnt ++;
            }
        }
        System.out.println(cnt);
    }

    static boolean check(String words) {
        boolean[] check = new boolean[26];
        char prev = words.charAt(0);
        check[prev - 'a'] = true;

        for (int i=1; i<words.length(); i++) {
            char word = words.charAt(i);
            if (prev != word) {
                prev = word;
                if (check[word - 'a'] == true) {
                    return false;
                }
                check[i] = true;
            }
        }
        return true;
    }
}