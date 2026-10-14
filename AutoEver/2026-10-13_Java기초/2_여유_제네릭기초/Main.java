// Python: 리스트/딕셔너리에 아무 타입이나 섞어 넣을 수 있음
// Java: List<Integer>처럼 <> 안에 타입을 못박아야 함 — 그래프 인접리스트 만들 때 자주 나오는 모양
// 막히면 Answer.java 참고.

import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 예시: Map<Integer, List<Integer>> graph 만들어서 1에 {2,3} 넣고 add(4)로 하나 더 추가 후 출력
        // 예상 출력: [2, 3, 4]


        // 예시: List<int[]> edges 만들어서 {1,2,5}, {2,3,3} add 하고
        // for문으로 "e[0] -> e[1] (w=e[2])" 형태로 출력
        // 예상 출력:
        // 1 -> 2 (w=5)
        // 2 -> 3 (w=3)


        // 연습 1: Map<String,Integer> fruitCount = {"apple":5, "banana":9, "kiwi":2}
        // entrySet 순회하면서 값이 제일 큰 key 찾아서 "key: value" 출력
        // 예상 출력: banana: 9


        // 연습 2: List<List<Integer>> grid — 바깥 리스트 3칸을 "매번 new ArrayList<>()로" 채운 뒤
        // grid.get(0).add(10), get(1).add(20), get(2).add(30) 하고 grid 전체 출력
        // 예상 출력: [[10], [20], [30]]

    }
}
