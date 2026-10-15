// Python: 변수에 타입 안 붙임, int가 알아서 무한정 커짐 (bignum)
// Java: 타입 명시 필수, int/long 자리수 한계 있음 → 코테에서 오버플로 버그 제일 많이 남
// 막히면 Answer.java 참고. 설명 보면서 직접 타이핑하고 실행해서 예상 출력이랑 맞는지 확인.

public class Main {
    public static void main(String[] args) {
        // 예시: int a=10, long b=10_000_000_000L(21억 넘으면 L 꼭 붙이기), double c=3.14 선언하고
        // a + " " + b + " " + c 형태로 한 줄 출력
        // 예상 출력: 10 10000000000 3.14
        int a = 10;
        long b = 10_000_000_000L;
        double c = 3.14;
        System.out.println(a + " " + b + " " + c);

        // 예시: int overflowed = Integer.MAX_VALUE + 1; 선언하고 출력
        // 예상 출력: int overflow: -2147483648
        int overflowed = Integer.MAX_VALUE + 1;
        System.out.println("int overflow: " + overflowed);

        // 연습 1: 곱셈 오버플로
        // int x = 1_000_000, y = 1_000_000;
        int x = 1_000_000;
        int y = 1_000_000;
        int wrong = x*y;
        System.out.println("wrong (int*int): " + wrong);

        // wrong = x * y (int끼리 곱함) 출력
        long correct = (long) x * y;
        System.out.println("correct (long) : " + correct);
        // correct = (long) x * y (곱하기 전에 캐스팅) 출력
        // stillWrong = x * y 를 long 변수에 대입만 한 것 (곱한 다음에 캐스팅한 꼴) 출력 — wrong이랑 같은 값 나오는지 확인
        // 예상 출력:
        // wrong (int*int): -727379968
        // correct (long): 1000000000000
        // still wrong (대입만 long): -727379968
        long stillWrong = x * y;
        System.out.println(stillWrong);


        // 연습 2: swap (임시변수 사용)
        // int p = 1, q = 2; 선언하고 temp 변수로 서로 바꾼 뒤 출력
        // 예상 출력: swapped: p=2, q=1
        int p = 1, q = 2;
        int temp = p;
        p = q;
        q = temp;
    }
}
