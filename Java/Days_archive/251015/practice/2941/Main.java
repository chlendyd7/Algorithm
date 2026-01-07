import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] words = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
        String inputs = br.readLine();
        
        for (String s : words) {
            inputs = inputs.replace(s, "a");
        }
        System.out.println(inputs.length());
    }
}