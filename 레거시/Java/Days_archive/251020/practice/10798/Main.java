import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char [][] board = new char[5][15];
    
        int maxLen = 0;
        for (int i=0; i<5; i++) {
            String curreString = br.readLine();

            if(curreString.length()>maxLen) {
                maxLen = curreString.length();
            }

            for (int j=0; j<curreString.length(); j++) {
                board[i][j] = curreString.charAt(j);
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int j=0; j<maxLen; j++) {
            for (int i=0; i<5; i++) {
                if(board[i][j] != '\u0000'){
                    sb.append(board[i][j]);
                }
            }
        }
        System.out.println(sb.toString());
    }
}