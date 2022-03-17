package If;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class A_2480 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str[] = br.readLine().split(" ");
		int first = Integer.parseInt(str[0]);
		int second = Integer.parseInt(str[1]);
		int third = Integer.parseInt(str[2]);
		
		if(first == second && second == third)
			System.out.print(10000+first*1000);
		else if(first == second || first == third)
			System.out.print(1000 + first*100);
		else if(second == third)
			System.out.print(1000+second*100);
		else
			System.out.print(Math.max(Math.max(first, second),third)*100);
		
		
	}
}
