package If;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class A_2753 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str[] = br.readLine().split(" ");
		int first = Integer.parseInt(str[0]);

		if((first%4 ==0 && first%100 !=0)|| first%400 ==0)
			System.out.print("1");
		else
			System.out.print("0");
	}
}
