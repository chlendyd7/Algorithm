def solution(n, left, right):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(max(i + 1, j + 1))  # 값 계산
        matrix.append(row)
    print(matrix)
    answer = []
    return answer
solution(3,2,5)


# def solution(n, left, right):
#     answer = []
#     for k in range(left, right + 1):
#         row = k // n
#         col = k % n
#         answer.append(max(row + 1, col + 1))
#     return answer
