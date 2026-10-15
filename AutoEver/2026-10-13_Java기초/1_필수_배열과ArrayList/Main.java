// Python: list 하나로 다 됨 (크기 자동 변경, 타입 안 가림)
// Java: 배열([])은 크기 고정, List<>(ArrayList 등)는 크기 가변 — 코테에서 언제 뭘 쓸지 헷갈리는 부분
// 막히면 Answer.java 참고.

import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 예시: int[] arr = new int[5]; arr[0]=1; 출력 (Arrays.toString 써야 배열이 제대로 보임)
        // 예상 출력: [1, 0, 0, 0, 0]
        int[] arr = new int[5];
        arr[0] = 1;
        System.out.println(Arrays.toString(arr));

        // 예시: ArrayList<Integer> list 만들어서 10, 20 add 하고, remove(0)(인덱스 기준 삭제) 한 뒤 출력
        // 예상 출력: [20]
        // List<Integer> list = new ArrayList<>();
        // list.add(10);
        // list.add(20);
        // list.remove(0);
        // System.out.println(list);


        // 연습 1: 2차원 배열 채우기
        // int[3][3] 만들고 이중 for문으로 전부 1 채운 뒤 Arrays.deepToString으로 출력
        // 예상 출력: [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        int[][] list = new int[3][3];
        for (int i = 0; i<3; i++) {
            for (int j=0; j<3; j++) {
                list[i][j] = 1;
            }
        }
        System.out.println(Arrays.deepToString(list));

        // 연습 2: 배열 깊은 복사
        // int[] original = {1,2,3}; int[] shallowRef = original; (대입만 함, 복사 아님)
        // shallowRef[0] = 999; 로 바꾼 뒤 original 출력해서 같이 바뀌는 거 확인
        // 예상 출력: original도 같이 바뀜: [999, 2, 3]
        int[] original = {1,2,3}; int[] shallowRef = original;
        shallowRef[0] = 999;
        System.out.println(Arrays.toString(original));
        //
        // int[] original2 = {1,2,3}; int[] deepCopy = Arrays.copyOf(original2, original2.length);
        // deepCopy[0] = 999; 로 바꾼 뒤 둘 다 출력해서 original2는 안 바뀌는 거 확인
        // 예상 출력:
        // original2는 안 바뀜: [1, 2, 3]
        // deepCopy만 바뀜: [999, 2, 3]
        int[] original2 = {1,2,3}; int[] deepCopy = Arrays.copyOf(original2, original2.length);
        deepCopy[0] = 999;
        System.out.println(Arrays.toString(original2));

        // 연습 3: List<Integer> -> int[] 변환
        // List<Integer> src = {1,2,3}; .stream().mapToInt(Integer::intValue).toArray() 로 변환 후 출력
        // 예상 출력: [1, 2, 3]
        List<Integer> src = new ArrayList<>(Arrays.asList(1,2,3));
        int[] converted = src.stream().mapToInt(Integer::intValue).toArray();
        System.out.println(Arrays.toString(converted));
    }
}
