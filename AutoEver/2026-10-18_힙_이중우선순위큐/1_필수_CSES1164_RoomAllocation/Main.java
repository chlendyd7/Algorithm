import java.io.*;
import java.util.*;

public class Main {
    static int[] allocateRooms(int[][] stays) {
        int n = stays.length;
        int[][] sortedRooms = new int[n][3];
        for (int i=0; i<n; i++) {
            sortedRooms[i][0] = stays[i][0];
            sortedRooms[i][1] = stays[i][1];
            sortedRooms[i][2] = i;
        }

        Arrays.sort(sortedRooms, (a,b) -> {
            if (a[0] == b[0]) return Integer.compare(a[1], b[1]);
            return Integer.compare(a[0], b[0]);
        });

        PriorityQueue<Integer> availableRoom = new PriorityQueue<>(); //빈 방 위치
        PriorityQueue<int[]> usedRoom = new PriorityQueue<>((a,b) -> Integer.compare(a[0], b[0])); // [departure, 있는 위치]

        int roomNumber = 1;
        int[] answer = new int[n];
        
        
        for (int i=0; i<n; i++) {
            int arrive = sortedRooms[i][0];
            int departure = sortedRooms[i][1];
            int originIdx = sortedRooms[i][2];

            while(!usedRoom.isEmpty() && usedRoom.peek()[0] < arrive) {
                availableRoom.add(usedRoom.poll()[1]);
            }

            int assignRoom;
            if (availableRoom.isEmpty()) {
                assignRoom = roomNumber++;
            } else {
                assignRoom = availableRoom.poll();
            }

            answer[originIdx] = assignRoom;
            usedRoom.add(new int[] {departure ,assignRoom});
        }

        return answer;
    }

    // 바이트 단위로 직접 빠르게 읽어오는 FastScanner
    static class FastScanner {
        private final InputStream in = System.in;
        private final byte[] buffer = new byte[1024 * 64];
        private int head = 0, tail = 0;

        private int read() {
            if (head >= tail) {
                head = 0;
                try {
                    tail = in.read(buffer, 0, buffer.length);
                } catch (IOException e) {
                    tail = -1;
                }
                if (tail <= 0) return -1;
            }
            return buffer[head++];
        }

        int nextInt() {
            int c = read();
            while (c <= 32) {
                if (c == -1) return -1;
                c = read();
            }
            int res = 0;
            while (c > 32) {
                if (c < '0' || c > '9') {
                    // 숫자 외의 문자가 들어올 경우 처리 (필요시)
                } else {
                    res = res * 10 + c - '0';
                }
                c = read();
            }
            return res;
        }
    }

    public static void main(String[] args) {
        FastScanner in = new FastScanner();
        int n = in.nextInt();
        if (n == -1) return;
        
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