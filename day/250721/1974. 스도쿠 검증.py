def solution(square):
    for i in range(9):
        row = set()
        col = set()
        for j in range(9):
            row.add(square[i][j])
            col.add(square[j][i])
        if len(row) != 9 or len(col) != 9:
            return 0

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            mat = set()
            for di in range(3):
                for dj in range(3):
                    mat.add(square[i + di][j + dj])
            if len(mat) != 9:
                return 0
    return 1


T = int(input())
for t in range(1, T+1):
    square = [list(map(int,input().split())) for _ in range(9)]
    print(f'#{t} {solution(square)}')

