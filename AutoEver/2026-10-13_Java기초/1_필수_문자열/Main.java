// Python: s1 == s2 로 내용 비교 가능, 문자열 자르기/합치기 쉬움
// Java: ==는 주소 비교라 문자열엔 쓰면 안 됨 (equals 써야 함) — 코테에서 제일 흔한 실수

public class Main {
    public static void main(String[] args) {
        // 예시: equals vs ==
        String a = new String("hello");
        String b = new String("hello");
        System.out.println(a == b);       // false — 서로 다른 객체라서
        System.out.println(a.equals(b));  // true — 내용 비교는 이걸로

        // 예시: StringBuilder — 문자열 반복해서 이어붙일 때 String끼리 +하면 매번 새 객체 생겨서 느림
        StringBuilder sb = new StringBuilder();
        sb.append("a").append("b").append("c");
        System.out.println(sb.toString());

        // TODO 1: "apple,banana,orange" 를 split(",")으로 나눠서 배열로 만들고 하나씩 출력해보기.


        // TODO 2: substring으로 문자열 자르기.
        // String s = "programmers" 에서 "gram" 부분만 잘라서 출력해보기.
        // 힌트: s.substring(시작인덱스, 끝인덱스) — 끝인덱스는 포함 안 됨(Python 슬라이싱이랑 비슷)


        // TODO 3: 문자 하나씩 순회하면서 알파벳 개수 세기.
        // "hello world" 에서 'l'이 몇 번 나오는지 세서 출력해보기.
        // 힌트: s.charAt(i) == 'l' 로 비교 (char는 작은따옴표)

    }
}
