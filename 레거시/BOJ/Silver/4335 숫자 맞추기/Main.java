import java.io.*;
import java.util.*;

public class Main {
    static String lier = "Stan is dishonest";
    static String honest = "Stan may be honest";
    static String correct = "right on";
    static String highAnswer = "too high";
    static String lowAnswer = "too low";
    public static boolean isNumeric(String str) {
        try {
            Integer.parseInt(str);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;
        String result;
        int tempNumber;
        int low = 1;
        int high = 10;

        while (true) {
            line = br.readLine();
            if (line == null || line.equals("0")) break;

            int num = Integer.parseInt(line);
            String response = br.readLine();
            if (response.equals(highAnswer)) {
                high = Math.min(high, num-1);
            } else if (response.equals(lowAnswer)) {
                low = Math.max(low, num+1);
            } else {
                if (low <= num && num<= high) {
                    System.out.println(honest);
                } else  {
                    System.out.println(lier);
                }
                low = 1;
                high = 10;
            }
        }
    }
}