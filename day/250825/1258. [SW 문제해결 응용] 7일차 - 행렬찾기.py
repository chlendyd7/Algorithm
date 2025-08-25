def solution():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    arr = []
    for i in range(N):
        for j in range(N):
            if board[i][j]: #ij가 값이 있으면
                row, col = i, j
                while row < N and board[row][j]:
                    row += 1
                while col < N and board[i][col]:
                    col += 1
                size_r = row - i
                size_c = col - j
                arr.append((size_r * size_c, size_r, size_c))
                for r in range(size_r):
                    for c in range(size_c):
                        board[i+r][j+c] = 0
    arr.sort(key= lambda x: (x[0], x[1]))
    result = [str(len(arr))]
    for cost, r, c in arr:
        result.append(str(r))
        result.append(str(c))
    return ' '.join(result)


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')