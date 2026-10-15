// https://school.programmers.co.kr/learn/courses/30/lessons/42746

import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String[] arr = new String[numbers.length];

        for (int i=0; i<numbers.length; i++) {
            arr[i] = String.valueOf(numbers[i]);
        }

        Arrays.sort(arr, (a,b) -> (b+a).compareTo(a+b));

        if (arr[0].equals("0")) {
            return "0";
        }

        return String.join("", arr);
    }
}

public class Main {
    public static void main(String[] args) {
        int[] numbers = {6, 10, 2};
        Solution sol = new Solution();
        System.out.println(sol.solution(numbers));
    }
}
