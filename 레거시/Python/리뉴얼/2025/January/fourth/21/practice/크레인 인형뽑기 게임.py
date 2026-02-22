def solution(board, moves):
    stack = []
    answer = 0
    for move in moves:
        move -= 1
        for i in range(len(board)):
            if board[i][move]:
                stack.append(board[i][move])
                board[i][move] = 0
                break
    
            while len(stack) >= 2 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2
    
    return answer