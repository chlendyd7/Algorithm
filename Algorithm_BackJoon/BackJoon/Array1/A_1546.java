package Array1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class A_1546 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		double array[] = new double[N];
		
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		
		
		for(int i=0; i<N; i++) {
			array[i] = Double.parseDouble(st.nextToken());
		}
		
		double sum =0;
		Arrays.sort(array);
		
		for(int i=0; i<N; i++) {
			sum+=((array[i] / array[array.length-1])*100);
		}
		System.out.print(sum/array.length);
	}
}
