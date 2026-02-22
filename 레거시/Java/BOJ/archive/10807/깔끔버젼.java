import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 깔끔버젼 {
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int i = Integer.parseInt(bf.readLine()); // 첫 번째 입력
        int count = 0; //찾는 숫자 개수를 셀 변수
        int v = 0; //찾는 숫자

        String[] numbers = bf.readLine().split(" ");

        v = Integer.parseInt(bf.readLine());

        for(int j=0; j<i; j++) {
            if(Integer.parseInt(numbers[j]) == v){
                count++;
            }
        }
        System.out.println(count);
    }
}
