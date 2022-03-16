package If;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class A_2884 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str[] = br.readLine().split(" ");
		int h = Integer.parseInt(str[0]);
		int m = Integer.parseInt(str[1]);

		if(m <45) {
			h --;
			m += 60;
		}
		if(h<0) {
			h += 24;
		}
		System.out.print(h);
		System.out.print(" ");
		System.out.print(m-45);
	
	}
}
