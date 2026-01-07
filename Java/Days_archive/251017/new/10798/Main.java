import java.io.*;
import java.util.*;
/*
 * A~z 0~9
 * 
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        char[][] board = new char[5][15];
        
        // 가장 긴 문자열의 길이를 저장(세로 읽기의 최대 열 인덱스를 결정하기 위함)
        int maxLen = 0;
        
        for (int i=0; i<5; i++) {
            String curreString = br.readLine();
            
            if (curreString.length() > maxLen) {
                maxLen = curreString.length();
            }
            
            for (int j=0; j< curreString.length(); j++) {
                board[i][j] = curreString.charAt(j);
            }
        }
        StringBuilder sb = new StringBuilder();

        for (int j=0; j<maxLen; j++) {
            for (int i=0; i<5; i++) {
                // 배열을 char 타입으로 선언했기 때문에, 값이 없는 칸은 널 문자('\u0000')로 초기화되어 있습니다.
                // 따라서 값이 널 문자가 아닌 경우에만 append 합니다.
                if (board[i][j] != '\u0000') {
                    sb.append(board[i][j]);
                }
            }
        }
        System.out.print(sb.toString());
    }
}
