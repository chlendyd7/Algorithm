package ab;

public class p_61 {

	class ReverseArray {
		static void swap(int a[], int idx1, int idx2) {
			int t = a[idx1];
			a[idx1] = a[idx2];
			a[idx2] = t;
		}

		static void reverse(int a[]) {
			for (int i = 0; i < a.length / 2; i++) {
				swap(a, i, a.length - i - 1);
			}
		}
	}

		public static void main(String[] args) {
			
			int a[] = { 5, 10, 73, 2, -5, 42 };

			for (int i = 0; i < a.length; i++) {
				System.out.print(a[i] + ", ");

			}
			reverse(a);

			for (int i = 0; i < a.length; i++) {
				System.out.print(a[i] + ", ");
			}
		}

	}

