// https://school.programmers.co.kr/learn/courses/30/lessons/64064

class Solution {
    String[] uId;
    String[] bId;
    boolean[] visited;
    HashSet<String> resultSet;
    
    public int solution(String[] user_id, String[] banned_id) {
        uId = user_id;
        bId = banned_id;
        visited = new boolean[used_id.length];
        resultSet = new HashSet<>();
        
        
        int answer = 0;
        return answer;
    }
    
    void dfs(int depth; List<String> current) {
        if (depth == bId.length) {
            List<String> sortedList = new ArrayList<>(current);
            Collections.sort(sortedList);
            resultSet.add(sortedList.toString());
            return
        }
        
        for (int i=0; i<uId.length; i++) {
            if(!visited[i] && isMatch(uId[i], bId[depth])) {
                visited[i] = true;
                current.add(uId[i]);
                dfs(depth+1, current);
                current.remove(current.size()-1);
                visited[i] = false;
            }
        }
    }
    
    boolean isMatch(String userId, String bannedId) {
        if (userId.length() != bannedId.length()) return false;
        
        for (int i=0; i<userId.length(); i++) {
            char b = bannedId.charAt(i);
            if (b == '*') continue;
            if (b!= userId.charAt(i)) return false;
        }
        return true;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution());
    }
}
