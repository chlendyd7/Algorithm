import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def solution():
    N = int(input())
    chus = list(map(int, input().split()))
    total_sum = sum(chus)  # 남은 추 계산용
    cnt = 0

    used = [False] * N

    def dfs(left, right, depth, remain):
        nonlocal cnt
        if left < right:  # 가지치기: 오른쪽이 더 무거우면 불가능
            return
        if depth == N:
            cnt += 1
            return

        for i in range(N):
            if not used[i]:
                used[i] = True
                # 왼쪽에 올리기
                dfs(left + chus[i], right, depth + 1, remain - chus[i])
                # 오른쪽에 올리기
                # 남은 추 합 + 오른쪽 합 >= 왼쪽 합이어야 올릴 수 있음
                if right + chus[i] <= left:
                    dfs(left, right + chus[i], depth + 1, remain - chus[i])
                used[i] = False

    dfs(0, 0, 0, total_sum)
    return cnt

T = int(input())
for t in range(1, T + 1):
    print(f"#{t} {solution()}")
