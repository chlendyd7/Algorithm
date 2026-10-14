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

        // ── 연습 1: 곱셈 오버플로 ────────────────────────────
        // int는 약 ±21억(2.1 * 10^9)까지만 담을 수 있음.
        // 1,000,000 * 1,000,000 = 10^12 인데 이건 int 범위를 훌쩍 넘어감 → 계산이 틀어짐.
        int x = 1_000_000;
        int y = 1_000_000;
        int wrong = x * y; // int * int 는 결과도 int로 계산 → 담다가 넘쳐서 틀린 값
        System.out.println("wrong (int*int): " + wrong);

        // 고치는 법: 피연산자 중 하나만 long으로 캐스팅해도 그 연산 전체가 long으로 승격됨
        long correct = (long) x * y; // (long) x 가 먼저 적용되고, 그 다음 곱셈은 long 연산
        System.out.println("correct (long): " + correct);

        // 흔한 함정: long correct2 = x * y; 라고만 쓰면 이미 int*int에서 틀어진 뒤에
        // long에 대입하는 거라 똑같이 틀림. 캐스팅은 "곱하기 전에" 해야 함.
        long stillWrong = x * y;
        System.out.println("still wrong (대입만 long): " + stillWrong);

        // ── 연습 2: swap (임시변수 사용) ──────────────────────
        // Python: a, b = b, a 처럼 한 줄로 되지만 Java는 그런 문법이 없음.
        int p = 1, q = 2;
        int temp = p; // p를 잃어버리기 전에 temp에 저장
        p = q;
        q = temp;
        System.out.println("swapped: p=" + p + ", q=" + q); // p=2, q=1
    }
}
