import java.util.*;

public class pract{
    static int[] allocateRooms(int[][] stays) {
        int n = stays.length;
        int[][] indexStays = new int[n][3];
        for (int i=0; i<n; i++) {
            indexStays[i][0] = stays[i][0];
            indexStays[i][1] = stays[i][1];
            indexStays[i][2] = i;
        }

        Arrays.sort((a,b) -> {
            if(a[0] == b[0]) return Integer.comapre(a[1], b[1]);
            return Integer.compare(a[0], b[0]);
        });


        PriorityQueue<Integer> availableRooms = new PriorityQueue<>();
        PriorityQueue<int[]> activeRooms = new PriorityQueue<>((a,b) -> Integer.compare(a[0], b[0]));
        int[] result = new int[n];
        int nextRoomNumber = 1;

        for (int i=0; i<n; i++) {
            int arrive = indexStays[i][0];
            int departure = indexStays[i][1];
            int idx = indexStays[i][2];

            // 현재 도착한 게 departure 최소보다 크면 사용 가능하니까
            while (!activeRooms.isEmpty() && activeRooms.peek()[0] < arrive) {
                int[] finished = activeRooms.poll();
                availableRooms.add(finished[1]);

            }
            int assignEdRoom;
            if (availableRooms.isEmpty()) {
                assignEdRoom = nextRoomNumber++;
            } else {
                assignEdRoom = availableRooms.poll();
            }

            result[idx] = assignEdRoom;
            activeRooms.add(new int[]{departure, assignedRoom});
        }
    }
}
