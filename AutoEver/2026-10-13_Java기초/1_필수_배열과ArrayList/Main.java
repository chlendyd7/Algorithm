// Python: list 하나로 다 됨 (크기 자동 변경, 타입 안 가림)
// Java: 배열([])은 크기 고정, List<>(ArrayList 등)는 크기 가변 — 코테에서 언제 뭘 쓸지 헷갈리는 부분

import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 예시: 배열 — 크기 고정, 선언할 때 크기 정해야 함
        int[] arr = new int[5];
        arr[0] = 1;
        System.out.println(Arrays.toString(arr));

        // 예시: ArrayList — 크기 가변, 추가/삭제 자유로움
        List<Integer> list = new ArrayList<>();
        list.add(10);
        list.add(20);
        list.remove(0); // 인덱스로 삭제 (Integer.valueOf(10)이면 값으로 삭제 — 헷갈리는 함정)
        System.out.println(list);

        // TODO 1: 2차원 배열 int[3][3] 만들고 전부 1로 채운 뒤 출력해보기.
        // 힌트: for문 이중으로 돌면서 arr2d[i][j] = 1


        // TODO 2: 배열을 "깊은 복사"해보기.
        // int[] original = {1,2,3} 만들고, int[] copy = original 로 대입한 뒤 copy[0]을 바꿔보면
        // original도 같이 바뀜 (참조 복사라서). Arrays.copyOf(original, original.length)로
        // 진짜 복사본 만들어서 copy[0] 바꿔도 original은 안 바뀌는 거 확인해보기.


        // TODO 3: ArrayList<Integer>를 int[]로 바꾸는 상황 자주 생김.
        // list에 1,2,3 넣고 int[]로 변환해서 출력해보기.
        // 힌트: list.stream().mapToInt(Integer::intValue).toArray()

    }
}
