import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        int R;
        String words;
        for (int i=0; i<T; i++) {
            String[] inputs = br.readLine().split(" ");
            R = Integer.parseInt(inputs[0]);
            words = inputs[1];
            for (int j=0; j<words.length(); j++) {
                char ch = words.charAt(j);
                for (int k=0; k<R; k++) {
                    System.out.print(ch);
                }
            }
            System.err.println();
        }
    }
}
