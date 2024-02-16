def solution(brown, red):
    total = brown + red
    col = 0
    row = 0
    for i in range(3, total+1):
        if total % i == 0:
            col = i
            row = total//i
            if (col - 2 ) * (row-2) == red:
                return[row, col]
print(solution(10, 2))