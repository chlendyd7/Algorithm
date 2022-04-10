package Array1;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class A_2562 {
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int array[] = new int[9];
		int big = 0;
		int index=0;

		for (int i = 0; i < array.length; i++) {
			array[i] = Integer.parseInt(br.readLine());
			
			if (array[i] > big) {
				big = array[i];
				index = i+1;
			}
		}
		System.out.println(big);
		System.out.println(index);
	}
}
