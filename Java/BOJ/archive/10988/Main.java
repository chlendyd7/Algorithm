import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String inputs = br.readLine(); // 테스트 케이스 수
        boolean check = false;
        for (int i = 0; i < inputs.length() / 2; i++) {
            if (inputs.charAt(i) != inputs.charAt(inputs.length() - i - 1)){
                System.out.print(0);
                check = true;
                break;
            }
        }
        if (!check) {
            System.err.println(1);
        }
    }
}
