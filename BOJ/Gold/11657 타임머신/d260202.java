import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class d260202 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] firstLine = br.readLine().split(" ");
        Integer n = Integer.parseInt(firstLine[0]);
        Integer m = Integer.parseInt(firstLine[1]);
        
        int [][] graph = new int[m][3];
        for (int i=0; i<m; i++) {
            String[] lines = br.readLine().split(" ");
            graph[i][0] = Integer.parseInt(lines[0]);
            graph[i][1] = Integer.parseInt(lines[1]);
            graph[i][2] = Integer.parseInt(lines[2]);
        }

        long[] result = bellmanford(1, n, m, graph);
        if (result == null) {System.err.println(-1);}
        else {
            for (int i=0; i<n; i++) {
                if (result[i] != Long.MAX_VALUE) 
                System.err.println();
                else System.out.println(-1);
            }
        }
    }

    public static long[] bellmanford(int start, int n, int m, int[][] graph) {
        long[] result = new long[m+1];
        Arrays.fill(result, Long.MAX_VALUE);
        result[start] = 0;
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                int u = graph[j][0];
                int v = graph[j][1];
                int w = graph[j][2];
                if (result[u] != Long.MAX_VALUE && result[v] > result[u] + w) {
                    result[v] = result[u] + w;
                    if (i == n-1) {
                        return null;
                    }
                }
            }
        }
        return result;
    }
}