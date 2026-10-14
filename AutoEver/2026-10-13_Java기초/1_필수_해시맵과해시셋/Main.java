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

        // TODO 1: 문자열 배열 {"a","b","a","c","b","a"} 에서 각 문자 등장 횟수를
        // HashMap<String, Integer>에 세서 저장하고 전부 출력해보기.
        // 힌트: map.put(key, map.getOrDefault(key, 0) + 1)


        // TODO 2: HashMap을 순회하면서 key, value 같이 꺼내기.
        // 위에서 만든 map을 for (Map.Entry<String,Integer> e : map.entrySet()) 로 순회해서
        // "key: value" 형태로 전부 출력해보기.

    }
}
