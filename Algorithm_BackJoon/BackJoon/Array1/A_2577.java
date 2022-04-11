package Array1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class A_2577 {
	public static void main(String[] args) throws IOException{
	
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int array[] = new int[10];
		
		int val = Integer.parseInt(br.readLine())*Integer.parseInt(br.readLine())*Integer.parseInt(br.readLine());
		
		String str = String.valueOf(val);
		
		for(int i=0; i<str.length(); i++) {
			array[(str.charAt(i)-'0')]++;
		}
		for(int i=0; i<array.length; i++) {
			System.out.println(array[i]);
		}
	}
}
