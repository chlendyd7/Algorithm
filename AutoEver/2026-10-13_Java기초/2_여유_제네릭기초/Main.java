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

        // ── 연습 1: Map에서 값이 제일 큰 key 찾기 ───────────────
        Map<String, Integer> fruitCount = new HashMap<>();
        fruitCount.put("apple", 5);
        fruitCount.put("banana", 9);
        fruitCount.put("kiwi", 2);

        String maxKey = null;
        int maxValue = Integer.MIN_VALUE; // 뭐가 와도 이것보단 크니까 시작값으로 안전함
        for (Map.Entry<String, Integer> e : fruitCount.entrySet()) {
            if (e.getValue() > maxValue) {
                maxValue = e.getValue();
                maxKey = e.getKey();
            }
        }
        System.out.println(maxKey + ": " + maxValue); // banana: 9

        // ── 연습 2: List<List<Integer>> 2차원 가변 구조 ─────────
        // Python 함정이랑 똑같이, Java도 [[]]*3 같은 식으로 하나의 리스트를 복제하면
        // 전부 "같은 리스트"를 가리키게 돼서 하나 바꾸면 전부 바뀌는 버그가 생김.
        // 그래서 바깥 리스트를 만든 뒤, 안쪽 리스트를 "하나씩 새로" 만들어서 넣어야 함.
        List<List<Integer>> grid = new ArrayList<>();
        for (int i = 0; i < 3; i++) {
            grid.add(new ArrayList<>()); // 매번 new로 새 리스트를 만들어서 add — 이게 핵심
        }
        grid.get(0).add(10);
        grid.get(1).add(20);
        grid.get(2).add(30);
        System.out.println(grid); // [[10], [20], [30]] — 서로 독립적으로 잘 들어감

        // 참고: 틀린 예시 (실제로 실행 안 함, 설명용)
        // List<List<Integer>> wrong = new ArrayList<>();
        // List<Integer> inner = new ArrayList<>();
        // for (int i = 0; i < 3; i++) wrong.add(inner); // 매번 같은 inner를 넣음 → 전부 같은 리스트
    }
}
