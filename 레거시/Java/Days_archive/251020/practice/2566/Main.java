import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = 9;
        int max = 0;
        int r = 1;
        int c = 1;
        for (int i=0; i<N; i++) {
            String[] row = br.readLine().split(" ");
            for (int j=0; j<N; j++) {
                if (Integer.parseInt(row[j]) > max) {
                    max = Integer.parseInt(row[j]);
                    r = i+1;
                    c = j+1;
                }
            }
        }
        System.out.println(max);
        System.out.println(r + " "+ c);
    }
}