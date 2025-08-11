import heapq

T = int(input())


def dfs(field, sums, target):
    global maxNum, buff
    if sum(sums) > C:
        if maxNum < target - (sums[-1] ** 2):
            maxNum = target - (sums[-1] ** 2)
        return
    for i in range(len(field)):
        if visited[i] == 0:
            visited[i] = 1
            dfs(field, sums + [field[i]], target + (field[i] ** 2))
            visited[i] = 0


for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    heap = []
    for r in range(N):
        for c in range(N - M + 1):
            maxNum = 0
            if sum(arr[r][c:c + M]) <= C:#모든벌통의 꿀을 채취할 수 있는 경우
                for s in arr[r][c:c + M]:
                    maxNum += s ** 2
            else:  # C 미만의 벌통을 선택해야하는 경우
                visited = [0] * M
                dfs(arr[r][c:c + M], [], 0)
            heapq.heappush(heap, (-maxNum, r, c))  # 최대힙
    answer = []
    while heap:
        num, row, col = heapq.heappop(heap)
        if len(answer) == 2: break
        if len(answer) == 1 and answer[0][1] == row:
            if abs(answer[0][2] - col) <= M - 1:#두 일꾼의 벌통이 겹치는 경우
                continue
        answer.append((num, row, col))
    print(f'#{tc} {-answer[0][0] - answer[1][0]}')
