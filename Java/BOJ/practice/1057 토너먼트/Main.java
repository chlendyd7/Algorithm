import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        // BufferedReader를 사용하여 입력을 빠르게 받습니다.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // 입력받은 한 줄을 split(" ")으로 나누어 배열에 저장합니다.
        String[] input = br.readLine().split(" ");
        
        // N은 전체 인원수이지만, 이 문제의 로직상 직접적으로 쓰이지는 않습니다.
        int n = Integer.parseInt(input[0]);
        int jimin = Integer.parseInt(input[1]);
        int hansu = Integer.parseInt(input[2]);
        
        int round = 0;
        
        // 김지민과 임한수의 번호가 같아질 때까지 반복합니다.
        // 번호가 같아진다는 것은 해당 라운드에서 대결한다는 뜻입니다.
        while (jimin != hansu) {
            // (번호 + 1) / 2를 수행하여 다음 라운드 번호를 갱신합니다.
            jimin = (jimin + 1) / 2;
            hansu = (hansu + 1) / 2;
            
            // 라운드 수를 증가시킵니다.
            round++;
        }
        
        // 결과 출력
        System.out.println(round);
    }
}
