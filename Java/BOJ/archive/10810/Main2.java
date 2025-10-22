import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
/**
 * 바구니 1~ N까지 번호
 * 바구니에는 공을 1개만 넣을 수 있다
 * M번 공을 넣으려고 한다
 * 
 * 
 * input
 * N,M
 * i, j, k i~j까지 k번 적혀있는 공을 넣음
 */

public class Main2 {
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = bf.readLine().split(" ");
        int N = Integer.parseInt(inputs[0]);
        int M = Integer.parseInt(inputs[1]);
        int[] basket = new int[N]; 
    
        int i,j,k;
        for (int l=0; l<M; l++) {
            String[] inputs2 = bf.readLine().split(" ");

            i = Integer.parseInt(inputs2[0]);
            j = Integer.parseInt(inputs2[1]);
            k = Integer.parseInt(inputs2[2]);

            for (int i2 = i - 1; i2 < j; i2++) {
                basket[i2] = k;
            }
        }
        for (int i = 1; i <= N; i++) {
            System.out.print(basket[i] + " ");
        }

        StringBuilder sb = new StringBuilder();
        for (int ball : basket) {
            sb.append(ball).append(" ");
        }
        System.out.println(sb.toString().trim());
    }
}