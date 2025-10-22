import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = 9;
        int[][] board = new int[9][9];
        int r = 0;
        int c = 0;
        int max = -1;

        for (int i=0; i<N; i++) {
            String[] row = br.readLine().split(" ");
            for (int j=0; j<N; j++) {
                if (max < Integer.parseInt(row[j])) {
                    max = Integer.parseInt(row[j]);
                    r = i+1;
                    c = j+1;
                }
            }
        }
        System.out.println(max);
        System.out.print(r + " " + c);
    }
}