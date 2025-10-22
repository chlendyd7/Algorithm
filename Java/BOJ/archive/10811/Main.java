import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void reverse(int[] arr, int start, int end) {
        // start가 end보다 작거나 같은 동안 반복
        while (start < end) {
            // 양 끝 값(start, end)을 교환
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            
            // 시작 인덱스는 증가, 끝 인덱스는 감소하며 중앙으로 이동
            start++;
            end--;
        }
    }
    public static void main(String[] args) throws IOException{
        int N, M;
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        String[] s = bf.readLine().split(" ");
        N = Integer.parseInt(s[0]);
        M = Integer.parseInt(s[1]);
        
        int[] basket = new int[N];
        for (int i=0; i<N; i++) basket[i] = i+1;


        for (int a=0; a<M; a++){
            s = bf.readLine().split(" ");
            int i = Integer.parseInt(s[0]);
            int j = Integer.parseInt(s[1]);

            reverse(basket, i-1, j-1);
        }

        StringBuilder sb = new StringBuilder();
        for (int ball : basket) {
            sb.append(ball).append(" ");
        }
        System.out.println(sb.toString().trim());
    }    
}
