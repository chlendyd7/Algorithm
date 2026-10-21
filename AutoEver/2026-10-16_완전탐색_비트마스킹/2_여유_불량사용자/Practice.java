import java.util.*;

class Solution {
    String[] uId;
    String[] bId;
    boolean[] visited;
    HashSet<String> set;

    public int solution(String[] user_id, String[] banned_id) {
        uId = user_id;
        bId = banned_id;
        visited = new boolean[uId.length];
        set = new HashSet<>();
        dfs(0, new ArrayList<>());
        return set.size();
    }

    void dfs(int depth, List<String> current) {
        if (depth == bId.length) {
            List<String> sortedList = new ArrayList<>(current);
            Collections.sort(sortedList);
            set.add(sortedList.toString());
            return;
        }

        for (int i=0; i<uId.length; i++) {
            if (!visited[i] && check(uId[i], bId[depth])) {
                visited[i] = true;
                current.add(uId[i]);
                dfs(depth+1, current);
                current.remove(current.size()-1);
                visited[i] = false;
            }
        }
    }

    boolean check(String user, String ban) {
        if (user.length() != ban.length()) return false;
        for (int i=0; i<user.length(); i++) {
            char b = ban.charAt(i);
            if (b=='*') continue;
            if (b!= user.charAt(i)) return false;
        }
        return true;
    }
}


public class Practice {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution(new String[] {"frodo", "fradi", "crodo", "abc123", "frodoc"}, 
            new String[] {"fr*d*", "abc1**"}
        ));
    }
}
