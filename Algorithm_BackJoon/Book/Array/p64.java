package Array;

public class p64 {

	static void copy(int[] a, int[] b) {
		for (int i = 0; i < b.length; i++) {
			a[i] = b[i];
		}
		
	}

	static void ReverseArray(int[] a, int idex1, int idex2) {
		int t = a[idex1];
		a[idex1] = a[idex2];
		a[idex2] = t;
	}

	static void rcopy(int[] a, int[] b) {
		copy(a, b);
		for (int i = 0; i < b.length / 2; i++) {
			ReverseArray(a, i, b.length - i - 1);
		}
		printArray(a);
	}

	static void printArray(int[] a) {
		for (int i = 0; i < a.length; i++) {
			System.out.print(a[i]);
		}
		System.out.println("\n");
	}

	static boolean equals(int[] a, int[] b) {
		if (a.length != b.length)
			return false;

		for (int i = 0; i < a.length; i++) {
			if (a[i] != b[i])
				return false;
		}
		return true;
	}

	public static void main(String[] args) {
		int a[] = { 1, 2, 3, 4, 5 };
		int b[] = { 5, 6, 7, 8, 9 };

		printArray(a);
		copy(a, b);
		printArray(a);
		rcopy(a, b);

		// System.out.println("배열 a와 b는" + (equals(a, b)? "같습니다": "같지 않습니다"));

	}
}
