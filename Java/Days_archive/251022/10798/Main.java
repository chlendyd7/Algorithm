import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = 5;
        char[][] board = new char[N][15];
        
        int maxLen = -1;
        
        for (int i=0; i<N; i++) {
            String row = br.readLine();
            int rowLen = row.length();
            if (maxLen<rowLen) maxLen=rowLen;
            
            for (int j=0; j<rowLen; j++) {
                board[i][j] = row.charAt(j);
            } 
        }
        
        StringBuilder sb = new StringBuilder();
        for (int j=0; j<maxLen; j++) {
            for (int i=0; i<N; i++) {
                char word = board[i][j];
                if (word != '\u0000') {
                    sb.append(word);
                }
            }
        }
        System.out.println(sb.toString());
    }
}
