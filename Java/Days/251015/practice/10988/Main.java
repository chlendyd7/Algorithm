import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String inputs = br.readLine();
        int N = inputs.length();
        boolean check = false;
        for (int i=0; i<inputs.length()/2; i++) {
            if (inputs.charAt(i) != inputs.charAt(N-i-1)) {
                check = true;
                break;
            }
        }
        System.out.println(check ? 0:1 );
    }
}