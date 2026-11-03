// https://www.geeksforgeeks.org/problems/largest-sum-cycle--170645/1

import java.util.*;

class Solution {
    public int largestSumCycle(int[] edge) {
        int n = edge.length;
        int[] stamp = new int[n];
        Arrays.fill(stamp, -1);
        int max = -1;

        // System.out.println(Arrays.toString(stamp));  // 제출 전 삭제 (출력 느림)
        for (int i = 0; i < n; i++) {
            if (stamp[i] != -1) continue;

            // int now = edge[i];                       // 버그: edge[i]==-1이면 edge[-1] 예외, i 자신 stamp 안 찍힘
            int now = i;

            // while (edge[now] != -1 && stamp[now] == -1) {  // 버그: 끝 노드(edge==-1) stamp 안 찍힘
            while (now != -1 && stamp[now] == -1) {
                stamp[now] = i;
                now = edge[now];
            }

            // if (edge[now] != -1 && stamp[now] == i) {      // now==-1 가능, edge[-1] 위험
            if (now != -1 && stamp[now] == i) {
                // int temp = now;                            // now를 두 번 더하게 됨
                int sum = now;

                // for (int j=now; j != i; j=edge[now]) {     // 버그: j != i (i는 꼬리일 수 있음), edge[now] (now 안 변함)
                //     temp += now;                           // 버그: j가 아니라 now를 더함
                // }
                for (int j = edge[now]; j != now; j = edge[j]) {
                    sum += j;
                }
                max = Math.max(max, sum);
            }
        }
        return max;
    }
}