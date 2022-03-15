package If;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class A_1330 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] str = br.readLine().split(" ");
		int first = Integer.parseInt(str[0]);
		int second = Integer.parseInt(str[1]);
		
		
		System.out.println((first>second)? ">" :((first < second)? "<" : "=="));
		
		
	}

}
