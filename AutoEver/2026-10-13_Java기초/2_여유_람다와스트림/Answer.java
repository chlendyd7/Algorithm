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

        // ── 연습 1: 최댓값 구하기 ────────────────────────────
        // mapToInt로 기본형 스트림(IntStream)으로 바꾼 다음 .max() 호출
        // .max()는 값이 없을 수도 있다고 가정해서 OptionalInt를 리턴 → .getAsInt()로 실제 값 꺼냄
        int max = nums.stream().mapToInt(Integer::intValue).max().getAsInt();
        System.out.println("max: " + max); // 5

        // ── 연습 2: 문자열을 길이 기준으로 정렬 ─────────────────
        // for문 버전(2_여유_Comparator와정렬에서 한 것)과 비교해보면
        // .sorted()에 Comparator 넣는 거라 사실상 구조는 똑같음 — 그냥 체이닝으로 쓰는 것뿐
        List<String> words = Arrays.asList("apple", "kiwi", "banana");
        List<String> sorted = words.stream()
                .sorted((a, b) -> a.length() - b.length())
                .collect(Collectors.toList());
        System.out.println(sorted); // [kiwi, apple, banana]

        // 결론: stream은 "짧게 쓰는 문법"일 뿐, for문으로 짠 것보다 더 똑똑한 게 아님.
        // 급하면 이거 몰라도 for문 + Comparator만으로 코테 전체 풀 수 있음.
    }
}
