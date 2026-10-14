// Python: dict, set 그대로 매핑됨
// Java: HashMap<K,V>, HashSet<T> — get/put/containsKey처럼 메서드 이름이 달라서 헷갈림
// 막히면 Answer.java 참고.

import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 예시: Map<String,Integer> map 만들어서 "apple",1 / "banana",2 put 하고
        // map.get("apple"), map.getOrDefault("grape",0), map.containsKey("banana") 각각 출력
        // 예상 출력:
        // 1
        // 0
        // true


        // 예시: Set<Integer> set 만들어서 1을 두 번 add 하고 size() 출력 (중복 무시되는지 확인)
        // 예상 출력: 1


        // 연습 1: 등장 횟수 세기
        // String[] arr = {"a","b","a","c","b","a"} 에서 각 문자 개수를
        // Map<String,Integer> counter에 getOrDefault 패턴으로 세서 저장하고 통째로 출력
        // 예상 출력 (순서는 HashMap이라 다를 수 있음, 값만 맞으면 됨): {a=3, b=2, c=1}


        // 연습 2: Map 순회하면서 key, value 같이 꺼내기
        // 위 counter를 for (Map.Entry<String,Integer> e : counter.entrySet()) 로 순회해서
        // "key: value" 형태로 출력
        // 예상 출력 (순서 상관없음):
        // a: 3
        // b: 2
        // c: 1

    }
}
