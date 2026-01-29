import java.io.*;
import java.util.*;

public class Main {
    static String[][] pictures = new String[10][3];
    static Set<String> allHapCombi = new HashSet<>();
    static Set<String> checkS = new HashSet<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i <= 9; i++) {
            String[] lines = br.readLine().split(" ");
            pictures[i][0] = lines[0];
            pictures[i][1] = lines[1];
            pictures[i][2] = lines[2];
        }

        for (int i = 0; i <= 7; i++) {
            for (int j = i + 1; j <= 8; j++) {
                for (int k = j + 1; k <= 9; k++) {
                    if (check(i, j, k)) {
                        allHapCombi.add(i + " " + j + " " + k);
                    }
                }
            }
        }
        int n = Integer.parseInt(br.readLine());
        int result = 0;
        boolean end = false;

        for (int i = 0; i < n; i++) {
            String[] cmd = br.readLine().split(" ");

            if (cmd[0].equals("H")) {
                int[] v = { Integer.parseInt(cmd[1]), Integer.parseInt(cmd[2]), Integer.parseInt(cmd[3]) };
                Arrays.sort(v);
                String key = v[0] + " " + v[1] + " " + v[2];

                if (allHapCombi.contains(key) && !checks.contains(key)) {
                    result += 1;
                    checkS.add(key);
                } else {
                    result -= 1;
                }
            } else if (cmd[0].equals("G")) {
                if (allHapCombi.size() == checkS.size() && !end) {
                    result += 3;
                    end = true;
                } else {
                    result -= 1;
                }
            }
        }
        System.out.println(result);
    }

    static boolean check(int i, int j, int k) {
        for (int attrIdx = 0; attrIdx < 3; attrIdx++) {
            Set<String> attrSet = new HashSet<>();
            attrSet.add(pictures[i][attrIdx]);
            attrSet.add(pictures[i][attrIdx]);
            attrSet.add(pictures[k][attrIdx]);

            if (attrSet.size() == 2)
                return false;
        }
        return true;
    }
}  