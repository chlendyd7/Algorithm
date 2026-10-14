// https://school.programmers.co.kr/learn/courses/30/lessons/42576

class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> pMap = new HashMap<>();
        HashMap<String, Integer> cMap = new HashMap<>();
        
        for (String p : participant) {
            pMap.put(p, pMap.getOrDefault(p, 0) + 1);
        }
        for (String c : completion) {
            cMap.put(c, cMap.getOrDefault(c, 0) + 1);
        }
        for (Map.Entry<String, Integer> entry : pMap.entrySet()) {
            String key = entry.getKey();
            Integer value = entry.getValue();
            
            if (cMap.get(key) == null) {
                return key;
            } else if (!value.equals(cMap.get(key))) {
                return key;
            }
        }
        return "";
    }
}
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution());
    }
}
