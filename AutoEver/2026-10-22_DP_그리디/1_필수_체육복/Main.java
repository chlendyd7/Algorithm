// https://school.programmers.co.kr/learn/courses/30/lessons/42862

public int solution(int n, int[] lost, int[] reserve) {
    int[] cnt = new int[n + 2];              // 0, n+1은 경계(항상 0이라 빌려줄 수 없음)
    for (int i = 1; i <= n; i++) cnt[i] = 1;
    for (int r : reserve) cnt[r]++;
    for (int l : lost) cnt[l]--;

    for (int i = 1; i <= n; i++) {
        if (cnt[i] == 0) {
            if (cnt[i - 1] == 2) { cnt[i - 1]--; cnt[i]++; }
            else if (cnt[i + 1] == 2) { cnt[i + 1]--; cnt[i]++; }
        }
    }
    int answer = 0;
    for (int i = 1; i <= n; i++) if (cnt[i] >= 1) answer++;
    return answer;
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution());
    }
}
