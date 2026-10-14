// Python: 변수에 타입 안 붙임, int가 알아서 무한정 커짐 (bignum)
// Java: 타입 명시 필수, int/long 자리수 한계 있음 → 코테에서 오버플로 버그 제일 많이 남

public class Main {
    public static void main(String[] args) {
        // 예시: 기본 타입 선언
        int a = 10;
        long b = 10_000_000_000L; // int 범위(약 21억) 넘으면 L 붙여서 long
        double c = 3.14;

        System.out.println(a + " " + b + " " + c);

        // 예시: int 오버플로 직접 보기
        int overflowed = Integer.MAX_VALUE + 1; // 2147483647 + 1 => 음수로 뒤집힘
        System.out.println("int overflow: " + overflowed);

        // TODO 1: 1,000,000 * 1,000,000 을 int로 곱하면 오버플로 남 (약 10^12인데 int는 약 21억까지).
        // int 변수에 곱해서 틀린 값 나오는 거 확인하고, long으로 캐스팅해서 올바른 값도 출력해보기.
        // 힌트: (long) a * b 처럼 피연산자 하나만 캐스팅해도 전체가 long 연산이 됨.


        // TODO 2: Python에서 a, b = b, a 처럼 스왑하던 거, Java는 임시변수 없이는 안 됨.
        // int x = 1, y = 2 선언하고 임시변수 써서 swap한 뒤 출력해보기.

    }
}
