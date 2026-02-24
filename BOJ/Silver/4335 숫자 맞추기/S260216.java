import java.io.*;
import java.util.*;

public class S260216 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;
        int value;
        int high = 10;
        int low = -1;

        while (true) {
            line = br.readLine();
            if (line.equals("0")) break;
            value = Integer.parseInt(line);
            String cmd = br.readLine();
            if (cmd.equals("too high")) {
                high = Math.min(high, value - 1);
            } else if (cmd.equals("too low")) {
                low = Math.max(low, value + 1);
            } else {
                if (low <= value && value <= high) {
                    System.out.println("Stan may be honest");
                } else {
                    System.out.println("Stan is dishonest");
                }
                high = 10;
                low = -1;
            }
        }
    }
}