'''
Java.BOJ.practice.2643 색종이 올려놓기.main의 Docstring
아이디어
먼저 한 변을 정렬해 맞춰둔다
dp를 이용해 뒤쪽 board가 나보다 작다면 해당 dp의 +1을 해준다
'''

N = int(input())
board = []

# 짧은 것 앞에 오게
for _ in range(N):
    a, b = map(int, input().split())
    if a > b:
        board.append((b,a))
    else:
        board.append((a,b))

board.sort(key= lambda x: (-x[0], -x[1]))
print(board)
dp = [1] * N

for i in range(N):
    for j in range(i): # 내 앞에 있는(나보다 큰) 종이들을 검사
        # 앞의 종이 j가 현재 종이 i를 포함할 수 있는가?
        # 가로는 이미 정렬로 보장됨(board[j][0] >= board[i][0])
        # 세로만 체크: board[j][1] >= board[i][1]
        if board[j][1] >= board[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp)) # 쌓인 최대 개수 출력
