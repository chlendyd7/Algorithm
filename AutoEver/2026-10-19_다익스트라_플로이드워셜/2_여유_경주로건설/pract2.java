import java.util.*;

class Solution {
    int[] dx = {1,-1,0,0};
    int[] dy = {0,0,1,-1};

    public int solution(int[][] board) {
        int n = board.length;
        int m = board[0].length;
        
        int [][][] graph = new int[n][m][4];
        for(int[][] a: graph) for (int[] b: a) Arrays.fill(b, Integer.MAX_VALUE);
        // x,y,d,cost
        PriorityQueue<int[]> pq = new PriorityQueue<>((x,y) -> Integer.compare(x[3], y[3]));

        for (int i=0; i<4; i++) {
            graph[0][0][i] = 0;
            pq.offer(new int[] {0,0,i,0});
        }
        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int x = curr[0];
            int y = curr[1];
            int d = curr[2];
            int cost = curr[3];

            if (graph[x][y][d] < cost) continue;
            for (int i=0; i<4; i++) {
                int nx = x+dx[i];
                int ny = y+dy[i];
                int nCost = cost + 100 + (d==i ? 0:500);
            
                if (nx >= 0 && ny >= 0 && nx <n && ny < m) {
                    if (graph[nx][ny][i] > nCost && board[nx][ny] == 0) {
                        pq.offer(new int[]{nx, ny, i, nCost});
                        graph[nx][ny][i] = nCost;
                    }
                }
            }
        }

        int answer = Integer.MAX_VALUE;
        for (int i=0; i<4; i++) {
            answer = Math.min(answer, graph[n-1][m-1][i]);
        }
        return answer;
    }
}
