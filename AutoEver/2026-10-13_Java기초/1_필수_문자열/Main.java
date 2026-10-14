// Python: s1 == s2 로 내용 비교 가능, 문자열 자르기/합치기 쉬움
// Java: ==는 주소 비교라 문자열엔 쓰면 안 됨 (equals 써야 함) — 코테에서 제일 흔한 실수
// 막히면 Answer.java 참고.

public class Main {
    public static void main(String[] args) {
        // 예시: String a = new String("hello"), b = new String("hello") 만들고 a==b, a.equals(b) 둘 다 출력
        // 예상 출력:
        // false
        // true


        // 예시: StringBuilder로 "a","b","c" append해서 이어붙인 뒤 출력
        // 예상 출력: abc


        // 연습 1: split으로 나누기
        // "apple,banana,orange" 를 split(",")으로 나눠서 for문으로 하나씩 출력
        // 예상 출력:
        // apple
        // banana
        // orange


        // 연습 2: substring으로 자르기
        // String s = "programmers"; substring(3, 7) 로 잘라서 출력 (끝 인덱스는 포함 안 됨)
        // 예상 출력: gram


        // 연습 3: 문자 하나씩 순회하며 개수 세기
        // "hello world" 에서 charAt(i) == 'l' 인 걸 세서 출력
        // 예상 출력: l 개수: 3

    }
}
