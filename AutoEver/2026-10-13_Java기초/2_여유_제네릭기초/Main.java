// Python: 리스트/딕셔너리에 아무 타입이나 섞어 넣을 수 있음
// Java: List<Integer>처럼 <> 안에 타입을 못박아야 함 — 코테에서는 깊게 안 써도 되지만
// List<int[]>, Map<String, List<Integer>> 같은 중첩은 자주 나와서 읽을 줄은 알아야 함

import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 예시: 제네릭 중첩 — 그래프 인접리스트 만들 때 제일 많이 쓰는 모양
        Map<Integer, List<Integer>> graph = new HashMap<>();
        graph.put(1, new ArrayList<>(Arrays.asList(2, 3)));
        graph.get(1).add(4);
        System.out.println(graph.get(1)); // [2, 3, 4]

        // 예시: List<int[]> — "간선 목록" 같은 걸 담을 때 자주 씀 (MST, 다익스트라 등)
        List<int[]> edges = new ArrayList<>();
        edges.add(new int[]{1, 2, 5}); // {from, to, weight}
        edges.add(new int[]{2, 3, 3});
        for (int[] e : edges) {
            System.out.println(e[0] + " -> " + e[1] + " (w=" + e[2] + ")");
        }

        // TODO 1: Map<String, Integer>를 하나 만들어서 과일별 개수를 넣고,
        // 값(개수)이 제일 큰 key를 찾아서 출력해보기.
        // 힌트: entrySet() 순회하면서 max 추적


        // TODO 2: List<List<Integer>>로 2차원 구조 만들기 (배열의 배열이 가변 버전인 느낌).
        // 크기 3짜리 바깥 리스트 만들고, 각 안쪽 리스트에 숫자 하나씩 넣어서 출력해보기.
        // 힌트: 바깥 리스트 만들 때 new ArrayList<>()를 미리 3번 add 해둬야 함
        //      (Python처럼 [[]]*3 하면 전부 같은 리스트를 가리켜서 버그남 — Java도 똑같이 조심)

    }
}
