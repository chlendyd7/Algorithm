// Python: [x*2 for x in nums if x > 0] 같은 컴프리헨션
// Java: stream().filter().map().collect() — 몰라도 for문으로 다 풀림, 급하면 스킵
// 막히면 Answer.java 참고.

import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) {
        List<Integer> nums = Arrays.asList(1, -2, 3, -4, 5);

        // 예시: nums에서 양수만 걸러서(filter) 2배로(map) 만든 뒤 리스트로 모아서(collect) 출력
        // 예상 출력: [2, 6, 10]
        List<Integer> result = nums.stream()
            .filter(x -> x > 0)
            .map(x -> x * 2)
            .collect(Collectors.toList());
        System.out.println(result);

        // 예시: mapToInt(Integer::intValue).sum() 으로 합계 출력
        // 예상 출력: 3
        int sum = nums.stream().mapToInt(Integer::intValue).sum();
        System.out.println(sum);

        // 예시: int[] {1,2,3} 은 Arrays.stream(arr).sum() 으로 합계 출력
        // 예상 출력: 6
        int[] arr = {1,2,3};
        int arrSum = Arrays.stream(arr).sum();
        System.out.println(arrSum);


        // 연습 1: nums에서 mapToInt().max().getAsInt() 로 최댓값 출력
        // 예상 출력: max: 5
        int max = nums.stream().mapToInt(Integer::intValue).max().getAsInt();
        System.out.println(5);


        // 연습 2: {"apple","kiwi","banana"} 를 stream().sorted((a,b)->a.length()-b.length())로
        // 길이순 정렬해서 출력
        // 예상 출력: [kiwi, apple, banana]
        String[] arr2 = {"apple", "kiwi", "banana"};
        String[] sortedArr = Arrays.stream(arr2).sorted((a,b) -> a.length() - b.length()).toArray(String[]::new);
        System.out.println(Arrays.toString(sortedArr));

                List<String> words = Arrays.asList("apple", "kiwi", "banana");
        List<String> sorted = words.stream()
                .sorted((a, b) -> a.length() - b.length())
                .collect(Collectors.toList());
        System.out.println(sorted); // [kiwi, apple, banana]
    }
}
