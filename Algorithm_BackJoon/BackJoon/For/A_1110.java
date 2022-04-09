package For;

import java.util.Scanner;

public class A_1110 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int a = sc.nextInt();
		int count = 1;
		int ten;
		int one;
		int plus;
		int finish = 0;

		one = a % 10;
		ten = a / 10;
		plus = one + ten;
		finish = (one * 10) + (plus % 10);
		System.out.println(finish);

		while (a != finish) {
			one = finish % 10;
			ten = finish / 10;
			plus = one + ten;
			finish = (one * 10) + (plus % 10);
			System.out.println(finish);
			count++;

		}
		System.out.println(count);

	}
}
