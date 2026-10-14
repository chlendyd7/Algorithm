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

    // 연습 1 정답: (0,0)인지 확인하는 인스턴스 메서드
    // this.x, this.y로 이 객체 자신의 필드에 접근함 (Python의 self.x랑 같은 개념)
    public boolean isOrigin() {
        return this.x == 0 && this.y == 0;
    }

    // static 메서드 — 객체 안 만들어도 클래스 이름으로 바로 호출 가능 (Point.add(..))
    static Point add(Point a, Point b) {
        return new Point(a.x + b.x, a.y + b.y);
    }
}

// 연습 2 정답: 프로그래머스 제출 코드의 실제 모양
// 클래스 이름은 항상 Solution, 메서드 이름은 항상 solution — 프로그래머스가 이 이름으로 호출하기 때문
class Solution {
    public int solution(int a, int b) {
        int answer = a + b;
        return answer;
    }
}

public class Main {
    public static void main(String[] args) {
        Point p = new Point(3, 4);
        System.out.println(p.distanceFromOrigin()); // 7
        System.out.println(p.isOrigin());            // false

        Point origin = new Point(0, 0);
        System.out.println(origin.isOrigin());       // true

        Point p2 = Point.add(p, new Point(1, 1));
        System.out.println(p2.x + " " + p2.y); // 4 5

        // 프로그래머스는 채점 서버가 "new Solution().solution(파라미터)"를 대신 호출해줌.
        // 로컬에서 테스트할 땐 이렇게 직접 객체를 만들어서 호출.
        Solution sol = new Solution();
        System.out.println(sol.solution(2, 3)); // 5
    }
}
