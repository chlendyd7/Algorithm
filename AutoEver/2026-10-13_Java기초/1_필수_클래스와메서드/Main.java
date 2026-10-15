// Python: def로 바로 함수 만들면 됨, class 없이도 코딩테스트 가능
// Java: 모든 코드가 class 안에 있어야 함 — 프로그래머스는 항상 "class Solution { solution() }" 패턴
// 막히면 Answer.java 참고.

// 예시: Point 클래스 만들기
// - 필드: int x, y
// - 생성자: Point(int x, int y) { this.x = x; this.y = y; }
// - 인스턴스 메서드: distanceFromOrigin() — Math.abs(x) + Math.abs(y) 리턴
// - static 메서드: add(Point a, Point b) — 새 Point(a.x+b.x, a.y+b.y) 리턴
class Point {
    int x, y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int distanceFromOrigin() {
        return Math.abs(x) + Math.abs(y);
    }

    public boolean isOrigin() {
        return this.x == 0 && this.y == 0;
    }

    static Point add(Point a, Point b) {
        return new Point(a.x + b.x, a.y+ b.y);
    }
}

// 연습 1: 위 Point 클래스 안에 isOrigin() 인스턴스 메서드 추가
// this.x == 0 && this.y == 0 인지 리턴

// 연습 2: 프로그래머스 제출 코드 실제 모양 연습
// class Solution { public int solution(int a, int b) { return a+b; } } 작성
// class Solution {
//
// }

public class Main {
    public static void main(String[] args) {
        Point p = new Point(3,4);
        // Point p = new Point(3, 4); 만들어서 p.distanceFromOrigin(), p.isOrigin() 출력
        // 예상 출력:
        // 7
        // false
        System.out.println(p.distanceFromOrigin());
        System.out.println(p.isOrigin());

        // Point origin = new Point(0, 0); 만들어서 origin.isOrigin() 출력
        // 예상 출력: true
        Point p2 = Point.add(p, new Point(1,1));
        System.out.println(p2.x + " " + p2.y);


        // Point.add(p, new Point(1,1)) 로 새 Point 만들어서 x, y 출력
        // 예상 출력: 4 5


        // Solution sol = new Solution(); 만들어서 sol.solution(2, 3) 출력
        // 예상 출력: 5

    }
}
