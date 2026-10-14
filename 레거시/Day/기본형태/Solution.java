import java.util.*;

class Solution {
    public static void main(String args[]) throws Exception {
        // 로컬 테스트 시 주석 제거
        // System.setIn(new FileInputStream("res/input.txt"));

        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int test_case = 1; test_case <= T; test_case++) {
            // 여기에 알고리즘 코드 작성
            System.out.println("#" + test_case + " " + solve(sc));
        }
        
        sc.close();
    }

    static String solve(Scanner sc) {
        // 입력 받기
        int N = sc.nextInt();
        
        // 알고리즘 로직
        
        // 결과 반환
        int result = 0;
        return String.valueOf(result);
    }
}
