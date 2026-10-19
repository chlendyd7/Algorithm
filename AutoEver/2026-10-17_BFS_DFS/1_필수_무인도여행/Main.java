// https://school.programmers.co.kr/learn/courses/30/lessons/154540
// 연습용: TODO 구현 전에는 실행 시 예외가 발생합니다.
import java.util.*;

class Solution {
    char[][] board;
    boolean[][] visited;
    int r,c;
    int[] dx = {1,-1,0,0};
    int[] dy = {0,0,1,-1};

    public int[] solution(String[] maps) {
        r = maps.length;
        c = maps[0].toCharArray().length;
        board = new char[r][c];
        visited = new boolean[r][c];
        for (int i=0; i<r; i++) {
                board[i] = maps[i].toCharArray();
        }

        List<Integer> list = new ArrayList<>();;
        for (int i=0; i<r; i++) {
            for (int j=0; j<c; j++) {
                int temp = 0;
                if (!visited[i][j] && board[i][j] != 'X') {
                    temp += bfs(i,j);
                    list.add(temp);
                }

            }
        }
        System.out.println(list);
        // TODO: 'X'는 바다, 숫자는 식량(일). 상하좌우로 이어진 칸이 한 섬.
        // 섬마다 식량 합을 구해 오름차순으로 반환. 섬이 하나도 없으면 {-1}.
        // 방문 배열 + BFS/DFS로 연결요소를 센다. maps[i].charAt(j) - '0'으로 숫자 변환.
        // 재귀 DFS는 격자가 최대 100x100이라 깊이 10,000 가능 → BFS(큐) 또는 스택 권장.
        // list.sort(Integer.compare((x,y) -> x-b));
        if (list.isEmpty()) return new int[] {-1};
        Collections.sort(list);

        return list.stream().mapToInt(Integer::intValue).toArray();
    }

    int bfs(int i1, int j1) {
        int cnt = board[i1][j1] - '0';
        Deque<int[] > q = new LinkedList<>();
        q.offer(new int[] {i1,j1});
        visited[i1][j1] = true;
        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int x = curr[0];
            int y = curr[1];

            for (int i=0; i<4; i++) {
                int nx = x+dx[i];
                int ny = y+dy[i];
                if (nx >= 0 && nx < r && ny >=0 && ny <c) {
                    if (board[nx][ny] != 'X' && !visited[nx][ny]) {
                        visited[nx][ny] = true;
                        cnt += board[nx][ny] - '0';
                        q.offer(new int[] {nx, ny});
                    }
                }
            }
        }
        return cnt;
    }
}

public class Main {
    static void check(int[] expected, int[] actual) {
        if (!Arrays.equals(expected, actual))
            throw new AssertionError("expected=" + Arrays.toString(expected) + ", actual=" + Arrays.toString(actual));
        System.out.println("PASS " + Arrays.toString(actual));
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        check(new int[]{1, 1, 27}, sol.solution(new String[]{"X591X", "X1X5X", "X231X", "1XXX1"}));
        check(new int[]{-1}, sol.solution(new String[]{"XXX", "XXX", "XXX"}));
        check(new int[]{5}, sol.solution(new String[]{"5"}));
    }
}
