import sys
from functools import lru_cache
input = sys.stdin.readline

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    balloons = list(map(int, input().split()))

    @lru_cache(None)
    def dfs(mask):
        """mask: 현재 터진 풍선 상태 비트마스크"""
        popped = [i for i in range(N) if not (mask & (1 << i))]

        if len(popped) == 1:  # 마지막 풍선
            return balloons[popped[0]]

        max_score = 0
        for i in popped:
            # 왼쪽 풍선
            left = next((balloons[j] for j in range(i - 1, -1, -1) if not (mask & (1 << j))), -1)
            # 오른쪽 풍선
            right = next((balloons[j] for j in range(i + 1, N) if not (mask & (1 << j))), -1)

            if left != -1 and right != -1:
                score = left * right
            elif left != -1:
                score = left
            elif right != -1:
                score = right
            else:
                score = balloons[i]

            # 풍선 i를 터뜨림
            max_score = max(max_score, score + dfs(mask | (1 << i)))
        return max_score

    print(f"#{tc} {dfs(0)}")
