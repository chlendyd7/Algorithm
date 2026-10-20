
import java.util.*;

class test {
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
}