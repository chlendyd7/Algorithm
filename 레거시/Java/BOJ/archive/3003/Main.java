import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int [] chess = {1,1,2,2,2,8};
        String [] inputs = br.readLine().split(" ");
        for (int i = 0; i < chess.length; i++) {
            int current = Integer.parseInt(inputs[i]);
            System.out.print((chess[i] - current) + " ");
        }
    }
}
