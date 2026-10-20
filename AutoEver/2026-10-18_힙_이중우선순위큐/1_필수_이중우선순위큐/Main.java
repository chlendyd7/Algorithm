// https://school.programmers.co.kr/learn/courses/30/lessons/42628

import java.util.*;



import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for(String op: operations) {
            String[] parts = op.split(" ");
            String cmd = parts[0];
            int val = Integer.parseInt(parts[1]);
            
            if(cmd.equals("I")) {
                minHeap.offer(val);
                maxHeap.offer(val);
                map.put(val, map.getOrDefault(val,0) + 1);
            } else {
                if (map.isEmpty()) continue;
                if(val == 1){
                    while(!maxHeap.isEmpty()) {
                        int max = maxHeap.poll();
                        if(map.getOrDefault(max, 0) > 0) {
                            map.put(max, map.get(max) - 1);
                            if(map.get(max) == 0) map.remove(max);
                            break;
                        }
                    }
                } else {
                    while(!minHeap.isEmpty()) {
                        int min = minHeap.poll();
                        if(map.getOrDefault(min, 0) > 0) {
                            map.put(min, map.get(min) - 1);
                            if(map.get(min) == 0) map.remove(min);
                            break;
                        }
                    }
                }
            }
        }
        if(map.isEmpty()) {
            minHeap.clear();
            maxHeap.clear();
        }
        while (!maxHeap.isEmpty() && map.getOrDefault(maxHeap.peek(), 0) == 0) {
            maxHeap.poll();
        } 
        while (!minHeap.isEmpty() && map.getOrDefault(minHeap.peek(), 0) == 0) {
            minHeap.poll();
        }
        if(maxHeap.isEmpty() || minHeap.isEmpty()) {
            return new int[] {0,0};
        }
        
        return new int[] {maxHeap.poll(), minHeap.poll()};
    }
}

// TreeMap 사용
// map.firstEntry() / map.lastEntry(): 가장 작은/큰 키와 값(Entry) 통째로 가져옵니다.
// map.pollFirstEntry() / map.pollLastEntry(): 가장 작은/큰 키와 값을 조회하면서 동시에 맵에서 제거합니다. (우선순위 큐의 poll처럼 쓸 수 있죠!)

class Solution {
    public int[] solution(String[] operations) {
        TreeMap<Integer, Integer> map = new TreeMap<>();

        for (String op : operations) {
            String[] parts = op.split(" ");
            String cmd = parts[0];
            int val = Integer.parseInt(parts[1]);

            if (cmd.equals("I")) {
                // 숫자를 넣고, 개수를 카운트 (중복 숫자 처리를 위해)
                map.put(val, map.getOrDefault(val, 0) + 1);
            } else {
                if (map.isEmpty()) continue;

                if (val == 1) {
                    // 최댓값 삭제 (lastKey)
                    int maxKey = map.lastKey();
                    if (map.get(maxKey) == 1) {
                        map.remove(maxKey);
                    } else {
                        map.put(maxKey, map.get(maxKey) - 1);
                    }
                } else {
                    // 최솟값 삭제 (firstKey)
                    int minKey = map.firstKey();
                    if (map.get(minKey) == 1) {
                        map.remove(minKey);
                    } else {
                        map.put(minKey, map.get(minKey) - 1);
                    }
                }
            }
        }

        if (map.isEmpty()) {
            return new int[] {0, 0};
        } else {
            return new int[] {map.lastKey(), map.firstKey()};
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution());
    }
}
