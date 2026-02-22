import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int X = Integer.parseInt(br.readLine());
        for (int i = 1; i <= X; i++) {
            String s = "*".repeat(i);
            s = (" ").repeat(X - s.length()) + s;
            System.out.println(s);
        }
        
    }    
}
