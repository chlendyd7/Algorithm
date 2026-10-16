// https://cses.fi/problemset/task/1164/
// 연습용: 입력/출력 틀만 제공. TODO 구현 전 실행하면 예외가 발생합니다.
import java.io.*;
import java.util.*;

public class Main {
    static int[] allocateRooms(int[][] stays) {
        // TODO: 입력 순서대로 각 손님의 방 번호(1-based)를 반환.
        // 연습 추가 조건: 사용할 수 있는 빈 방 중 가장 작은 번호를 선택.
        // 원문 경계: 기존 손님의 퇴실일 < 새 손님의 입실일일 때만 재사용 가능.
        throw new UnsupportedOperationException("TODO: 두 힙으로 방 배정");
    }

    static class TokenReader {
        private final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        private StringTokenizer st;

        int nextInt() throws IOException {
            while (st == null || !st.hasMoreTokens()) {
                String line = br.readLine();
                if (line == null) throw new EOFException("입력이 부족합니다.");
                st = new StringTokenizer(line);
            }
            return Integer.parseInt(st.nextToken());
        }
    }

    public static void main(String[] args) throws Exception {
        TokenReader in = new TokenReader();
        int n = in.nextInt();
        int[][] stays = new int[n][2];
        for (int i = 0; i < n; i++) {
            stays[i][0] = in.nextInt();
            stays[i][1] = in.nextInt();
        }
        int[] rooms = allocateRooms(stays);
        int roomCount = 0;
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < rooms.length; i++) {
            roomCount = Math.max(roomCount, rooms[i]);
            if (i > 0) out.append(' ');
            out.append(rooms[i]);
        }
        System.out.println(roomCount);
        System.out.println(out);
    }
}

