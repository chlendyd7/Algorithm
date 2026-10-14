// Python: [x*2 for x in nums if x > 0] 같은 컴프리헨션
// Java: stream().filter().map().collect() — 코테에서 필수는 아니지만 알아두면 짧게 씀
// (급하면 이 폴더는 제일 나중에 봐도 됨, 그냥 for문으로 짜도 전혀 문제없음)

import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) {
        List<Integer> nums = Arrays.asList(1, -2, 3, -4, 5);

        // 예시: filter + map — "양수만 걸러서 2배로" (Python: [x*2 for x in nums if x > 0])
        List<Integer> result = nums.stream()
                .filter(x -> x > 0)
                .map(x -> x * 2)
                .collect(Collectors.toList());
        System.out.println(result); // [2, 6, 10]

        // 예시: 합계 구하기 (Python: sum(nums))
        int sum = nums.stream().mapToInt(Integer::intValue).sum();
        System.out.println(sum);

        // 예시: int[] 배열은 바로 .stream() 안 되고 Arrays.stream() 써야 함
        int[] arr = {1, 2, 3};
        int arrSum = Arrays.stream(arr).sum();
        System.out.println(arrSum);

        // TODO 1: nums에서 최댓값을 stream으로 구해보기.
        // 힌트: nums.stream().mapToInt(Integer::intValue).max().getAsInt()


        // TODO 2: List<String> {"apple", "kiwi", "banana"} 를 길이 기준으로 정렬한
        // 새 리스트를 stream으로 만들어보기 (sorted 사용).
        // for문으로 짜는 거보다 짧아지는지 비교해보기 — 안 짧아지면 그냥 for문 써도 됨.

    }
}
