import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Integer N = Integer.parseInt(br.readLine());
        String[] input = br.readLine().split(" ");
        int[] tops = Arrays.stream(input)
                   .mapToInt(Integer::parseInt)
                   .toArray();
        
        int[] result = new int[N];
        Deque<int[]> stack = new ArrayDeque<>();

        for (int i=0; i<N; i++) {
            int nowTop = tops[i];

            while (!stack.isEmpty() && stack.peek()[0] < nowTop) {
                stack.pop();
            }

            if(!stack.isEmpty()){
                result[i] = stack.peek()[1] + 1;
            } else {
                result[i] = 0;
            }

            stack.push(new int[]{nowTop, i});
        }
        
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<N; i++) {
            sb.append(result[i]).append(" ");
        }
        System.out.println(sb.toString().trim());
    }
}