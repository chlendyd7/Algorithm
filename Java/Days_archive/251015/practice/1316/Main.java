import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int result = 0;
        String inputs;
        int t = Integer.parseInt(br.readLine());
        for (int i=0; i<t; i++) {
            inputs = br.readLine();
            if (isGroup(inputs)) result ++;
        }
        System.out.println(result);
    }

    static boolean isGroup(String words) {
        boolean[] check = new boolean[26];
        char prev = 0;

        for (int i=0; i<words.length(); i++) {
            char c = words.charAt(i);
            
            if (c != prev) {
                if (check[c-'a']){
                    return false;
                }
                check[c-'a'] = true;
                prev = c;
            }
        }
        return true;
    }
}