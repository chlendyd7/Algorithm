'''
1. 두 개의 숫자판을 선택, 정해진 횟수 만큼 **자리를** 교환 할 수 있음
2. 오른쪽 끝에서부터 1원 왼쪽으로 갈 수록 10배수 커짐
3. 그냥 자리 수 대로 상금 획득
4. 가장 ㅡㅋㄴ 금액
'''
def solution():
    board, M = input().split()
    board = list(map(int, board))
    M = int(M)
    while M:
        check = False
        for i in range(len(board) - 1):
            if check:
                break
            for j in range(len(board)-1, i, -1):
                if board[i] < board[j]:
                    board[i], board[j] = board[j], board[i]
                    check = True
                    break
        if not check:
            board[-1], board[-2] = board[-2], board[-1]
        M -=1
    
    return ''.join(map(str, board))


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
