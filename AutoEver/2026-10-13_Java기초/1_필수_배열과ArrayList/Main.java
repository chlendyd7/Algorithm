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

        // ── 연습 1: 2차원 배열 채우기 ──────────────────────────
        // Python: [[1]*3 for _ in range(3)] 한 줄
        // Java는 바깥 for, 안쪽 for 이중으로 직접 돌아야 함.
        int[][] arr2d = new int[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                arr2d[i][j] = 1;
            }
        }
        System.out.println(Arrays.deepToString(arr2d)); // 2차원 배열 출력은 deepToString 써야 함

        // ── 연습 2: 배열 깊은 복사 ────────────────────────────
        // Java 배열 변수는 "주소"를 담고 있음 (Python 리스트도 사실 똑같이 참조형이라 마찬가지).
        int[] original = {1, 2, 3};
        int[] shallowRef = original;   // 복사가 아니라 같은 배열을 가리키는 것뿐
        shallowRef[0] = 999;
        System.out.println("original도 같이 바뀜: " + Arrays.toString(original)); // [999, 2, 3]

        int[] original2 = {1, 2, 3};
        int[] deepCopy = Arrays.copyOf(original2, original2.length); // 진짜 새 배열을 만들어서 값만 복사
        deepCopy[0] = 999;
        System.out.println("original2는 안 바뀜: " + Arrays.toString(original2)); // [1, 2, 3]
        System.out.println("deepCopy만 바뀜: " + Arrays.toString(deepCopy));      // [999, 2, 3]

        // ── 연습 3: List<Integer> -> int[] 변환 ────────────────
        List<Integer> src = new ArrayList<>(Arrays.asList(1, 2, 3));
        int[] converted = src.stream().mapToInt(Integer::intValue).toArray();
        // src.stream(): 리스트를 스트림으로 바꿈
        // .mapToInt(Integer::intValue): Integer(박싱된 객체) 하나하나를 int(기본형)로 풀어줌
        // .toArray(): int[] 로 모아줌
        System.out.println(Arrays.toString(converted));
    }
}
