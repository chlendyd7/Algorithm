// Python: list.sort(key=lambda x: x[1]) 처럼 key 함수 하나로 끝
// Java: Comparator 인터페이스를 구현해야 함 — 람다로 쓰면 Python이랑 비슷해짐
// (10/15 정렬 날에 본격적으로 쓸 핵심 문법이라 여기서 기본기만 먼저)

import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 예시: 배열 기본 정렬
        int[] arr = {5, 2, 4, 1, 3};
        Arrays.sort(arr); // 오름차순 고정, int[]는 Comparator 못 씀
        System.out.println(Arrays.toString(arr));

        // 예시: Integer[]나 List는 Comparator로 커스텀 정렬 가능
        List<Integer> list = new ArrayList<>(Arrays.asList(5, 2, 4, 1, 3));
        list.sort((a, b) -> b - a); // 람다 — Python의 key=lambda 느낌이지만 두 값을 직접 비교
        System.out.println(list);

        // 예시: 2차원 배열(쌍) 정렬 — 코테에서 제일 많이 씀
        int[][] pairs = {{1, 3}, {2, 1}, {3, 2}};
        Arrays.sort(pairs, (a, b) -> a[1] - b[1]); // 두 번째 값 기준 오름차순
        System.out.println(Arrays.deepToString(pairs));

        // Comparator 람다 (a, b) -> ... 읽는 법:
        // 음수 리턴 → a가 b보다 먼저 와야 함
        // 양수 리턴 → b가 a보다 먼저 와야 함
        // 0 리턴    → 순서 상관없음
        // 그래서 "a - b"면 오름차순, "b - a"면 내림차순이 됨 (Python에는 없는 개념이라 외워둬야 함)

        // ── 연습 1: 문자열을 길이 기준으로 정렬 ─────────────────
        List<String> words = new ArrayList<>(Arrays.asList("banana", "kiwi", "apple"));
        words.sort((a, b) -> a.length() - b.length()); // 길이가 짧은 게 먼저 오도록 오름차순
        System.out.println(words); // [kiwi, apple, banana]

        // ── 연습 2: "가장 큰 수" 패턴 — 숫자를 이어붙였을 때 제일 큰 조합 ──
        // {3, 30, 34} 를 이어붙여서 제일 큰 수를 만들려면: "34" + "330" vs "330" + "34" 를 비교해서
        // 더 큰 쪽이 앞에 오게 정렬해야 함 (단순 숫자 크기 비교로는 안 풀림 — 3 < 30 이지만 "334"보다 "330" 조합이 작음)
        Integer[] nums = {3, 30, 34};
        Arrays.sort(nums, (a, b) -> {
            String ab = "" + a + b; // a 뒤에 b를 이어붙인 문자열
            String ba = "" + b + a; // b 뒤에 a를 이어붙인 문자열
            return ba.compareTo(ab); // ba가 더 크면(문자열 비교) a가 앞으로 와야 하므로 내림차순 비교
        });
        StringBuilder sb = new StringBuilder();
        for (int num : nums) sb.append(num);
        System.out.println(sb); // 34330 (제일 큰 조합)
    }
}
