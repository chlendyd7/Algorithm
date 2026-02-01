import java.io.*;
import java.util.*;

public class Main {
    static final long INF = Long.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] firstLine = br.readLine().split(" ");
        int n = Integer.parseInt(firstLine[0]);
        int m = Integer.parseInt(firstLine[1]);

        int[][] edges = new int[m][3];
        for (int i = 0; i < m; i++) {
            String[] edgeLine = br.readLine().split(" ");
            edges[i][0] = Integer.parseInt(edgeLine[0]);
            edges[i][1] = Integer.parseInt(edgeLine[1]);
            edges[i][2] = Integer.parseInt(edgeLine[2]);
        }

        long[] result = ballmanFord(1, n, m, edges);

        if (result == null) {
            System.out.println(-1);
        } else {
            for (int i = 2; i <= n; i++) {
                if (result[i] != INF)
                    System.err.println(result[i]);
                else System.err.println(-1);
            }
        }

    }
    
    public static long[] ballmanFord(int start, int n, int m, int[][] edges) {
        long[] dist = new long[n + 1];
        Arrays.fill(dist, INF);
        dist[start] = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int u = edges[j][0];
                int v = edges[j][1];
                int w = edges[j][2];

                if (dist[u] != INF && dist[v] > dist[u] + w) {
                    dist[v] = dist[u] + w;

                    if (i == n - 1) {
                        return null;
                    }

                }
            }
        }
        return dist;
    }
}