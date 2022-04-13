package Array1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class A_3052 {
	public static void main(String[] args) throws IOException{
	
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		boolean array[] = new boolean [42];
		
		
		
		for(int i=0; i<10; i++) {
			array[Integer.parseInt(br.readLine()) %42 ] = true;
		}
		int count =0;
		for(boolean value : array) {
			if(value) {
				count++;
			}
		}
		System.out.println(count);
	}
}
