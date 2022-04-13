package Array1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class A_8958 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int N = Integer.parseInt(br.readLine());
		String array[] = new String[N];

		for (int i = 0; i < N; i++) {
			array[i] = br.readLine();
		}
		
		for(int i=0; i<N; i++) {
			
			int sum = 0;
			int cnt = 0;
		
			for (int j = 0; j < array[i].length(); j++) {
				if (array[i].charAt(j) == 'O') {
					cnt++;
				} else {
					cnt = 0;
				}
				sum += cnt;
			}
			sb.append(sum).append('\n');
			//System.out.println(sum);
		}
		System.out.print(sb);
	}
}
