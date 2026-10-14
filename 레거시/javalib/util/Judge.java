package util;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;

public class Judge {

    public static void check(Object actual) {
        checkImpl(String.valueOf(actual));
    }

    public static void check(int[] actual) {
        checkImpl(Arrays.toString(actual));
    }

    public static void check(Object[] actual) {
        checkImpl(Arrays.deepToString(actual));
    }

    private static void checkImpl(String actual) {
        String expected;
        try {
            expected = Files.readString(Paths.get("output.txt")).trim();
        } catch (Exception e) {
            System.out.println("output.txt를 읽을 수 없음: " + e.getMessage());
            return;
        }
        System.out.println("actual  : " + actual);
        System.out.println("expected: " + expected);
        System.out.println(actual.equals(expected) ? "PASS" : "FAIL");
    }
}
