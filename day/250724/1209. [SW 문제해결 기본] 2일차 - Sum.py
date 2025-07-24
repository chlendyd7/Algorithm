def solution():
    _ = input()
    lst = [list(map(int,input().split())) for _ in range(100)]
    max_row = 0
    col = [0] * 100
    dia = 0
    reverse_dia = 0
    for i in range(100):
        row = lst[i]
        max_row = max(max_row, sum(row))
        dia += lst[i][i]
        reverse_dia += lst[i][99-i]
        for j in range(100):
            col[j] += lst[i][j]

    return max(max_row, max(col), dia, reverse_dia)


for t in range(1, 11):
    print(f'#{t} {solution()}')
