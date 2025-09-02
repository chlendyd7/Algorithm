'''
    8개로 이루어짐
    7개의 비트로 암호화되어 주어짐(숫자 하나는) 가로길이 56
    올바른 암호코드 홀수자리의 합 x3 짝수 자리의 합이 10배수가 되어야함

    1개가 포함된 직사각형 배열을 읽는다
    암호코드 이외의 부분은 전부 0으로 주어짐?

    세로크기 N 배열의 가로크기 M
    0111011 
    0110001
    0111011
    0110001
    0110001
    0001101
    0010011
    0111011
'''
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    board = [list(map(int, input())) for _ in range(N)]

    idx = (0, 0)
    check = False
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                idx = (i, j)
                check = True
        if check:
            break
    
    print(idx)
    password = board[i][56:j+1]
    print(password)
    for i in ra
