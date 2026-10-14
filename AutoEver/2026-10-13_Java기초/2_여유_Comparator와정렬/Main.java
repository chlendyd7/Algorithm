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

        // TODO 1: {"banana", "kiwi", "apple"} 를 길이가 짧은 순서로 정렬해서 출력해보기.
        // 힌트: Arrays.asList(...)를 ArrayList로 감싼 뒤 .sort((a,b) -> a.length() - b.length())


        // TODO 2: "가장 큰 수"류 문제에서 쓰는 패턴 — 숫자를 문자열로 바꿔서 비교.
        // {3, 30, 34} 를 문자열로 이어붙였을 때 제일 큰 값이 되도록 정렬해보기 (정답: 34330).
        // 힌트: Comparator.comparing(x -> ..., 또는 (a,b) -> (b+a).compareTo(a+b))

    }
}
