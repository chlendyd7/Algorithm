package If;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class A_9498 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] str = br.readLine().split(" ");
		int testScore = Integer.parseInt(str[0]);
		
		/*
		 * if(testScore>89 && testScore < 101) System.out.print("A"); else
		 * if(testScore>=80 && testScore <= 89) System.out.print("B"); else
		 * if(testScore>=70 && testScore <= 79) System.out.print("C"); else
		 * if(testScore>=60 && testScore <= 69) System.out.print("D"); else
		 * System.out.print("F");
		 * 
		 * 
		 */
		System.out.print((testScore>=90)? "A" : (testScore>=80)? "B": (testScore >=70)? "C" : (testScore >=60)? "D" : "F");
	}

}
