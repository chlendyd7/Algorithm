import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;

public class Main {
    public static void main(String[] args) throws IOException{
        int n, m, a, b, index1, index2, tmp;
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String[] s = bf.readLine().split(" ");
        
        n = Integer.parseInt(s[0]);
        m = Integer.parseInt(s[1]);
        
        int[] basket = new int[n];
        for (int i=0; i<n; i++) {
            basket[i] = i+1;
        }
        
        for (int i=0; i<m; i++) {
            s = bf.readLine().split(" ");
            index1 = Integer.parseInt(s[0]) - 1;
            index2 = Integer.parseInt(s[1]) - 1;
            tmp = basket[index1];

            basket[index1] = basket[index2];
            basket[index2] = tmp;
        }

        StringBuilder sb = new StringBuilder();
        for (int ball : basket) {
            sb.append(ball).append(" ");
        }
        System.out.println(sb.toString().trim());

        
    }
}
