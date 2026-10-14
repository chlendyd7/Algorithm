// Python: list.sort(key=lambda x: x[1]) 처럼 key 함수 하나로 끝
// Java: Comparator 인터페이스를 구현해야 함 — 람다로 쓰면 Python이랑 비슷해짐
// 막히면 Answer.java 참고.

import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 예시: int[] {5,2,4,1,3} Arrays.sort로 오름차순 정렬해서 출력
        // 예상 출력: [1, 2, 3, 4, 5]


        // 예시: List<Integer> {5,2,4,1,3} 를 (a,b)->b-a 로 내림차순 정렬해서 출력
        // 예상 출력: [5, 4, 3, 2, 1]


        // 예시: int[][] {{1,3},{2,1},{3,2}} 를 두 번째 값 기준 오름차순(a,b)->a[1]-b[1] 정렬해서 출력
        // 예상 출력: [[2, 1], [3, 2], [1, 3]]


        // 연습 1: {"banana","kiwi","apple"} 를 길이 기준 오름차순 정렬해서 출력
        // 예상 출력: [kiwi, apple, banana]


        // 연습 2: "가장 큰 수" 패턴
        // Integer[] {3, 30, 34} 를 (a,b) -> (""+b+a).compareTo(""+a+b) 로 정렬해서 이어붙여 출력
        // 예상 출력: 34330

    }
}
