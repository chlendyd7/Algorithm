import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int M = N / 4;
        String repeatedLong = "long ".repeat(M);
        System.out.printf("%sint%n", repeatedLong);
    }
}
