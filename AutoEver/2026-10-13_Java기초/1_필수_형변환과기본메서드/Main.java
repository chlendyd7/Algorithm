// 점검하다 빠진 걸 발견해서 추가한 폴더 — 문자/숫자 변환, Math 메서드, Integer 비교 함정
// 셋 다 거의 모든 문제에서 최소 한 번은 쓰게 됨

public class Main {
    public static void main(String[] args) {
        // ── char <-> int 변환 ────────────────────────────────
        // Python: ord('a'), chr(97) 로 변환
        // Java: char는 사실 내부적으로 숫자(아스키코드)라서 그냥 산술 연산이 됨
        char c = 'a';
        int code = c; // char를 int에 대입하면 자동으로 아스키코드 숫자가 됨
        System.out.println("'a'의 아스키코드: " + code); // 97

        char back = (char) 97; // 숫자를 다시 char로 바꾸려면 명시적 캐스팅 필요
        System.out.println("97의 char: " + back); // a

        // 알파벳 순서 계산 — 코테에서 엄청 자주 씀 (예: 'a'~'z' 몇 번째 글자인지)
        char target = 'd';
        int indexFromA = target - 'a'; // char끼리 빼면 아스키코드 차이 = 순서 차이
        System.out.println("'d'는 'a'로부터 " + indexFromA + "번째"); // 3

        // 반대로 "n번째 알파벳"을 구할 때
        int n = 5;
        char nthLetter = (char) ('a' + n);
        System.out.println(n + "번째 알파벳: " + nthLetter); // f

        // 숫자 문자 '0'~'9'를 실제 숫자로 바꿀 때도 같은 원리
        char digitChar = '7';
        int digit = digitChar - '0';
        System.out.println("'7' -> " + digit); // 7 (int)

        // Character 클래스의 판별 메서드들 — Python의 .isdigit(), .isalpha()에 대응
        System.out.println(Character.isDigit('5'));     // true
        System.out.println(Character.isAlphabetic('a')); // true
        System.out.println(Character.isUpperCase('A'));  // true

        // ── Math 클래스 ──────────────────────────────────────
        // Python: max(a,b), min(a,b), abs(x), x**2 등 내장 함수/연산자
        // Java: Math.max, Math.min, Math.abs, Math.pow 등 static 메서드로 제공
        System.out.println(Math.max(3, 7));      // 7
        System.out.println(Math.min(3, 7));      // 3
        System.out.println(Math.abs(-5));        // 5
        System.out.println(Math.pow(2, 10));     // 1024.0 — 리턴값이 double이라 캐스팅 필요할 때 많음
        System.out.println((int) Math.pow(2, 10)); // 1024 (int로)
        System.out.println(Math.sqrt(16));       // 4.0

        // 배열/리스트 전체에서 최댓값 구할 땐 Math.max를 반복문 안에서 누적시킴 (Python의 max(list)는 없음)
        int[] arr = {3, 7, 1, 9, 4};
        int maxVal = arr[0];
        for (int v : arr) {
            maxVal = Math.max(maxVal, v);
        }
        System.out.println("배열 최댓값: " + maxVal); // 9

        // ── Integer 비교 함정 ─────────────────────────────────
        // Python은 숫자 비교에 항상 == 쓰면 됨. Java는 int(기본형)는 ==로 값 비교가 맞는데,
        // Integer(객체, 박싱된 타입)는 == 하면 "주소 비교"가 될 수 있어서 가끔 틀림.
        int p1 = 127, p2 = 127;
        System.out.println(p1 == p2); // true — 기본형(int)끼리는 항상 값 비교라 안전

        Integer i1 = 127, i2 = 127;
        System.out.println(i1 == i2); // true — 근데 이건 자바가 -128~127 범위를 캐싱해둬서 우연히 true인 것

        Integer i3 = 200, i4 = 200;
        System.out.println(i3 == i4); // false! 캐싱 범위 밖이라 서로 다른 객체 → 값은 같은데 비교는 틀림

        System.out.println(i3.equals(i4)); // true — Integer끼리는 항상 equals로 비교해야 안전함

        // 결론: HashMap<Integer,...>에서 꺼낸 값이나 List<Integer>에 담긴 값끼리 비교할 땐
        // == 말고 equals()를 쓰거나, int로 꺼내서(언박싱) 비교하는 습관을 들일 것.
    }
}
