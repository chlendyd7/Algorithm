package input_output;

import java.util.Scanner;

public class A_2588 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int first = sc.nextInt();
		int second = sc.nextInt();
		System.out.println(second%100);
		System.out.println(first*(second%10));
		System.out.println(first*(second%100)/10);
		System.out.println(first*(second - second%100)/100);
		System.out.println(first*second);
	}

}
