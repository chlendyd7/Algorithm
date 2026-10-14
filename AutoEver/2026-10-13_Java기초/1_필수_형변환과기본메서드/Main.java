// 문자/숫자 변환, Math 메서드, Integer 비교 함정 — 셋 다 거의 모든 문제에서 최소 한 번은 쓰게 됨
// 막히면 Answer.java 참고.

public class Main {
    public static void main(String[] args) {
        // char c = 'a'; int code = c; 로 아스키코드 뽑아서 출력
        // 예상 출력: 'a'의 아스키코드: 97


        // char back = (char) 97; 로 다시 문자로 바꿔서 출력
        // 예상 출력: 97의 char: a


        // char target = 'd'; int indexFromA = target - 'a'; 출력 (알파벳 순서 계산)
        // 예상 출력: 'd'는 'a'로부터 3번째


        // int n = 5; char nthLetter = (char)('a' + n); 출력 (반대 방향)
        // 예상 출력: 5번째 알파벳: f


        // char digitChar = '7'; int digit = digitChar - '0'; 출력
        // 예상 출력: '7' -> 7


        // Character.isDigit('5'), Character.isAlphabetic('a'), Character.isUpperCase('A') 각각 출력
        // 예상 출력:
        // true
        // true
        // true


        // Math.max(3,7), Math.min(3,7), Math.abs(-5), Math.pow(2,10), (int)Math.pow(2,10), Math.sqrt(16) 각각 출력
        // 예상 출력:
        // 7
        // 3
        // 5
        // 1024.0
        // 1024
        // 4.0


        // int[] arr = {3,7,1,9,4}; 를 돌면서 Math.max로 최댓값 누적시켜서 출력
        // 예상 출력: 배열 최댓값: 9


        // int p1=127, p2=127; (p1==p2) 출력
        // Integer i1=127, i2=127; (i1==i2) 출력
        // Integer i3=200, i4=200; (i3==i4) 출력, (i3.equals(i4)) 출력
        // 예상 출력:
        // true
        // true   (127은 캐싱 범위 안이라 우연히 true)
        // false  (200은 캐싱 범위 밖이라 서로 다른 객체)
        // true   (equals는 항상 값 비교라 안전)

    }
}
