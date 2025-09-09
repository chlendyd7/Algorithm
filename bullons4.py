import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    balloons = list(map(int, input().split()))
    ans = -1  # 최대 점수 저장

    def dfs(arr, total_score):
        nonlocal ans

        # 풍선이 1개 남으면 종료 (마지막 풍선 점수 더함)
        if len(arr) == 1:
            ans = max(ans, total_score + arr[0])
            return

        for i in range(len(arr)):
            # 현재 터뜨릴 풍선의 점수 계산
            if i == 0:
                score = arr[i + 1]            # 왼쪽 풍선 없음
            elif i == len(arr) - 1:
                score = arr[i - 1]            # 오른쪽 풍선 없음
            else:
                score = arr[i - 1] * arr[i + 1]  # 양쪽 풍선 모두 존재

            # 풍선 터뜨리기
            removed = arr.pop(i)
            dfs(arr, total_score + score)
            arr.insert(i, removed)  # 상태 복원

    dfs(balloons, 0)
    print(f"#{tc} {ans}")
