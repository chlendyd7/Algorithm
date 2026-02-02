import java.io.*;
import java.util.*;

public class Main {
    static final int INF = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        
        int[][] dist = new int[n+1][n+1];
        int[][] nxt = new int[n+1][n+1];

        for (int i=1; i<n+1; i++) {
            for (int j=1; j<n+1; j++) {
                if (i==j) dist[i][j] = 0;
                else dist[i][j] = INF;
            }
        }

        for (int i=0; i<m; i++) {
            String[] line = br.readLine().split(" ");
            int u = Integer.parseInt(line[0]);
            int v = Integer.parseInt(line[1]);
            int w = Integer.parseInt(line[2]);
        
            if (w < dist[u][v]) {
                dist[u][v] = w;
                nxt[u][v] = v;
            }
        }

        for (int k=1; k<n+1; k++) {
            for (int i=1; i<n+1; i++) {
                for (int j=1; j<n+1; j++) {
                    if (dist[i][j] > dist[i][k] + dist[k][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                        nxt[i][j] = nxt[i][k];
                    }
                }
            }
        }
    }
}