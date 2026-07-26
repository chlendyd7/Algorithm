# https://school.programmers.co.kr/learn/courses/30/lessons/92344
def solution(board, skill):
    N = len(board)
    M = len(board[0])
    
    tmp = [[0] * (M+1) for _ in range(N+1)]
    
    for type, r1, c1, r2, c2, degree in skill:
        degree = degree if type == 2 else -degree
        
        tmp[r1][c1] += degree
        tmp[r1][c2+1] -= degree
        tmp[r2+1][c1] -= degree
        tmp[r2+1][c2+1] += degree
    
    for r in range(N):
        for c in range(M):
            tmp[r][c+1] += tmp[r][c]
    
    for c in range(M):
        for r in range(N):
            tmp[r+1][c] += tmp[r][c]
    
    answer = 0
    for r in range(N):
        for c in range(M):
            if board[r][c] + tmp[r][c] > 0:
                answer += 1
    
    return answer
