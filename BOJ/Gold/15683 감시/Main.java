import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        initIO();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    }

    private static void initIO() {
        try {
            // 현재 클래스 위치 기반 경로 추출
            String path = Main.class.getResource("").getPath();
            File inputFile = new File(path + "input.txt");

            if (inputFile.exists()) {
                System.setIn(new FileInputStream(inputFile));
                System.setOut(new PrintStream(new FileOutputStream(path + "output.txt")));
            }
        } catch (Exception e) {
        }
    }
}