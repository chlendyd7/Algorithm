package Array;

public class p60 {
	
	static int sumOf(int a[]) {
		int sum = 0;
		for(int i=0; i<a.length; i++) {
			sum += a[i];
		}
		return sum;
	}
	static void swap(int[]a, int idx1, int idx2) {
		int t = a[idx1]; a[idx1] = a[idx2]; a[idx2] = t;
		
	}
	static void reverse(int[]a) {
		for(int i=0; i<a.length/2; i++) {
			swap(a, i, a.length-i-1);
		}
	}
	public static void main(String[] args) {
		int x[] = {5, 10, 73, 2, -5, 42};
		reverse(x);
		
		for(int i=0; i<x.length; i++) {
			System.out.println(x[i]);
			
		}
		System.out.println(sumOf(x));
	}
}
