package Array;

import java.util.Scanner;

public class p62 {
	static boolean equals(int []a, int[]b) {
		if(a.length !=b.length)
			return false;
		
		for(int i=0; i<a.length; i++) {
			if(a[i] != b[i])
				return false;
		}
		return true;
	}
	
	public static void main(String[] args) {
		int a[] = {1,2,3,4};
		int b[] = {1,2,3,4,5};
		
		System.out.println("배열 a와 b는" + (equals(a, b)? "같습니다": "같지 않습니다"));
		
	}
}
