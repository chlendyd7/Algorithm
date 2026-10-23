// 연습용: TODO 구현 전에는 실행 시 예외가 발생합니다.
// Python의 itertools / deque.rotate를 Java로 직접 쓰는 연습. 후기(DP, deque rotate, product/combinations 백트래킹) 대비.
// 원본 유형: 백준 15651(N과 M 3), 15650(N과 M 2), 15649(N과 M 1), 20055(컨베이어 벨트 위의 로봇의 deque rotate). 백준은 종료됨.
// 결과는 사전순으로 반환. 수는 1..n.
//   product       : 1..n에서 m개를 중복 허용, 순서 있게  (itertools.product(repeat=m))
//   combinations  : 1..n에서 m개를 중복 없이, 순서 없이  (itertools.combinations)
//   permutations  : 1..n에서 m개를 중복 없이, 순서 있게  (itertools.permutations)
//   rotate        : deque.rotate(k). k > 0이면 오른쪽으로 k칸, k < 0이면 왼쪽. k가 길이보다 커도 동작. ArrayDeque 사용 권장.
// 목표: 빈 화면에서 5분 안에 네 개를 다 쓴다.
import java.util.*;

class Solution {
    public List<int[]> product(int n, int m) {
        // TODO
        throw new UnsupportedOperationException("TODO");
    }

    public List<int[]> combinations(int n, int m) {
        // TODO
        throw new UnsupportedOperationException("TODO");
    }

    public List<int[]> permutations(int n, int m) {
        // TODO
        throw new UnsupportedOperationException("TODO");
    }

    public int[] rotate(int[] arr, int k) {
        // TODO
        throw new UnsupportedOperationException("TODO");
    }
}

public class Main {
    static void check(String name, Object expected, Object actual) {
        String e = Arrays.deepToString(expected instanceof List ? ((List<?>) expected).toArray() : new Object[]{expected});
        String a = Arrays.deepToString(actual instanceof List ? ((List<?>) actual).toArray() : new Object[]{actual});
        if (!e.equals(a)) throw new AssertionError(name + ": expected=" + e + ", actual=" + a);
        System.out.println("PASS " + name);
    }

    static void checkCount(String name, int expectedCount, List<int[]> list, int[] first, int[] last) {
        if (list.size() != expectedCount) throw new AssertionError(name + ": count expected=" + expectedCount + ", actual=" + list.size());
        if (!Arrays.equals(list.get(0), first)) throw new AssertionError(name + ": first=" + Arrays.toString(list.get(0)));
        if (!Arrays.equals(list.get(list.size() - 1), last)) throw new AssertionError(name + ": last=" + Arrays.toString(list.get(list.size() - 1)));
        for (int i = 1; i < list.size(); i++)
            if (Arrays.compare(list.get(i - 1), list.get(i)) >= 0) throw new AssertionError(name + ": not strictly increasing at " + i);
        System.out.println("PASS " + name + " (" + list.size() + ")");
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        check("product 3,2", List.of(new int[]{1,1}, new int[]{1,2}, new int[]{1,3}, new int[]{2,1}, new int[]{2,2},
                new int[]{2,3}, new int[]{3,1}, new int[]{3,2}, new int[]{3,3}), s.product(3, 2));
        check("combinations 4,2", List.of(new int[]{1,2}, new int[]{1,3}, new int[]{1,4}, new int[]{2,3},
                new int[]{2,4}, new int[]{3,4}), s.combinations(4, 2));
        check("permutations 3,2", List.of(new int[]{1,2}, new int[]{1,3}, new int[]{2,1}, new int[]{2,3},
                new int[]{3,1}, new int[]{3,2}), s.permutations(3, 2));

        checkCount("product 7,4", 2401, s.product(7, 4), new int[]{1,1,1,1}, new int[]{7,7,7,7});
        checkCount("combinations 10,5", 252, s.combinations(10, 5), new int[]{1,2,3,4,5}, new int[]{6,7,8,9,10});
        checkCount("permutations 8,4", 1680, s.permutations(8, 4), new int[]{1,2,3,4}, new int[]{8,7,6,5});
        checkCount("combinations m=n", 1, s.combinations(5, 5), new int[]{1,2,3,4,5}, new int[]{1,2,3,4,5});
        checkCount("product m=1", 3, s.product(3, 1), new int[]{1}, new int[]{3});

        int[] a = {1, 2, 3, 4, 5};
        check("rotate +2", new int[]{4, 5, 1, 2, 3}, s.rotate(a, 2));
        check("rotate 0", new int[]{1, 2, 3, 4, 5}, s.rotate(a, 0));
        check("rotate +7 (> len)", new int[]{4, 5, 1, 2, 3}, s.rotate(a, 7));
        check("rotate -1", new int[]{2, 3, 4, 5, 1}, s.rotate(a, -1));
        check("rotate -8 (> len)", new int[]{4, 5, 1, 2, 3}, s.rotate(a, -8));
        check("rotate empty", new int[]{}, s.rotate(new int[]{}, 3));
        check("input unchanged", new int[]{1, 2, 3, 4, 5}, a);
    }
}
