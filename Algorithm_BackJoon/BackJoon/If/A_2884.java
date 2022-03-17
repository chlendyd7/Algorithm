package If;

import java.util.Scanner;

public class A_2884 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int h = sc.nextInt();
		int m = sc.nextInt();
		int time = sc.nextInt();
		m += time;
		if (m >= 60) {
			while (m >= 60) {
				m -= 60;
				h++;
				if (h >= 24) {
					h = 0;
				}
			}
		}
		System.out.print(h + " " + m);

	}
}
