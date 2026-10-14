// Python: dict, set 그대로 매핑됨
// Java: HashMap<K,V>, HashSet<T> — get/put/containsKey처럼 메서드 이름이 달라서 헷갈림

import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 예시: HashMap 기본
        Map<String, Integer> map = new HashMap<>();
        map.put("apple", 1);
        map.put("banana", 2);
        System.out.println(map.get("apple"));              // 1
        System.out.println(map.getOrDefault("grape", 0));   // 없으면 기본값 0 (Python dict.get(key, 0)이랑 동일)
        System.out.println(map.containsKey("banana"));      // true

        // 예시: HashSet 기본
        Set<Integer> set = new HashSet<>();
        set.add(1);
        set.add(1); // 중복은 무시됨
        System.out.println(set.size()); // 1

        // ── 연습 1: 등장 횟수 세기 ─────────────────────────────
        // Python이면: from collections import Counter; Counter(arr)
        // Java는 Counter가 없어서 HashMap으로 직접 세야 함. 패턴은 코테에서 제일 많이 나옴.
        String[] arr = {"a", "b", "a", "c", "b", "a"};
        Map<String, Integer> counter = new HashMap<>();
        for (String key : arr) {
            // getOrDefault(key, 0): "이 key 본 적 있으면 그 값, 처음 보면 0"을 가져옴
            // 그 값에 +1 해서 다시 put → "처음 보면 1, 이미 있으면 기존값+1"이 됨
            // Python의 counter[key] = counter.get(key, 0) + 1 과 완전히 똑같은 동작
            counter.put(key, counter.getOrDefault(key, 0) + 1);
        }
        System.out.println(counter); // {a=3, b=2, c=1} (HashMap이라 순서는 보장 안 됨)

        // ── 연습 2: Map 순회하면서 key, value 같이 꺼내기 ────────
        // Python이면: for key, value in counter.items(): ...
        // Java는 .entrySet()을 돌려야 key/value 쌍(Map.Entry)이 나옴.
        // (map.keySet()만 돌리고 매번 map.get(key) 하는 것보다 entrySet이 더 빠름 — 조회를 한 번만 하니까)
        for (Map.Entry<String, Integer> e : counter.entrySet()) {
            System.out.println(e.getKey() + ": " + e.getValue());
        }

        // 참고: key만 필요하면 keySet(), value만 필요하면 values() 써도 됨
        // for (String key : counter.keySet()) { ... }
        // for (int value : counter.values()) { ... }
    }
}
