// Python: def로 바로 함수 만들면 됨, class 없이도 코딩테스트 가능
// Java: 모든 코드가 class 안에 있어야 함 — 프로그래머스는 항상 "class Solution { solution() }" 패턴

class Point {
    int x, y; // 필드

    // 생성자 — 객체 만들 때 초기값 넣어주는 특수 메서드, 클래스 이름이랑 같아야 함
    public Point(int x, int y) {
        this.x = x; // this.x는 필드, x는 매개변수 — 이름 같을 때 구분하려고 this 붙임
        this.y = y;
    }

    // 인스턴스 메서드 — 객체 만든 다음에만 호출 가능 (new Point(..).distance())
    public int distanceFromOrigin() {
        return Math.abs(x) + Math.abs(y);
    }

    // static 메서드 — 객체 안 만들어도 클래스 이름으로 바로 호출 가능 (Point.add(..))
    static Point add(Point a, Point b) {
        return new Point(a.x + b.x, a.y + b.y);
    }
}

public class Main {
    public static void main(String[] args) {
        Point p = new Point(3, 4);
        System.out.println(p.distanceFromOrigin()); // 7

        Point p2 = Point.add(p, new Point(1, 1));
        System.out.println(p2.x + " " + p2.y); // 4 5

        // TODO 1: Point에 "Point(0,0)인지 확인하는" isOrigin() 인스턴스 메서드를 위 class에 추가하고
        // 여기서 호출해서 true/false 출력해보기.


        // TODO 2: 프로그래머스 문제 풀 때 쓰는 실제 패턴 연습 —
        // 아래 class Solution을 만들고 solution(int a, int b) 메서드가 a+b를 리턴하게 작성한 뒤
        // main에서 new Solution().solution(2,3) 호출해서 출력해보기.
        // (프로그래머스 제출용 코드는 항상 이 모양: class Solution { public 리턴타입 solution(파라미터) {...} })

    }
}
