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

        // ── 연습 1: split으로 문자열 나누기 ─────────────────────
        // Python: "a,b,c".split(",") 그대로 대응됨
        String csv = "apple,banana,orange";
        String[] fruits = csv.split(",");
        for (String f : fruits) {
            System.out.println(f);
        }

        // ── 연습 2: substring으로 자르기 ────────────────────────
        // Python: s[시작:끝] 슬라이싱이랑 거의 같은데, Java는 메서드 호출로 씀
        String s = "programmers";
        // substring(시작인덱스, 끝인덱스) — 끝인덱스는 "포함 안 됨" (Python 슬라이싱이랑 동일 규칙)
        // p-r-o-g-r-a-m-m-e-r-s
        // 0 1 2 3 4 5 6 7 8 9 10
        // "gram" = 인덱스 3부터 6까지(7은 미포함)
        String sub = s.substring(3, 7);
        System.out.println(sub); // gram

        // ── 연습 3: 문자 하나씩 순회하며 개수 세기 ───────────────
        // Python: s.count('l') 한 방에 되지만 Java는 그런 메서드가 없어서 직접 순회해야 함
        String target = "hello world";
        int count = 0;
        for (int i = 0; i < target.length(); i++) {
            // charAt(i): i번째 문자를 char(문자 하나)로 반환. char는 작은따옴표로 씀 ('l')
            if (target.charAt(i) == 'l') {
                count++;
            }
        }
        System.out.println("l 개수: " + count); // 3
    }
}
