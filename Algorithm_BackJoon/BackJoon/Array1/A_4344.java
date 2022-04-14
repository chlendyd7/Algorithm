package Array1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class A_4344 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int[] array;
		int test_case = Integer.parseInt(br.readLine());

		for (int i = 0; i < test_case; i++) {

			st = new StringTokenizer(br.readLine(), " ");
			
			int array_long = Integer.parseInt(st.nextToken());
			 array = new int[array_long];
			double sum = 0;

			for (int j = 0; j < array_long; j++) {
				int val = Integer.parseInt(st.nextToken());
				array[j] = val;
				sum += val;
			}
			double mean = (sum / array_long);
			double count = 0;

			for (int j = 0; j < array_long; j++) {
				if (array[j] > mean) {
					count++;
				}
			}
			System.out.printf("%.3f%%\n", (count / array_long) * 100);
		}

	}
}
