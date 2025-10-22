# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu
'''
한변의 길이가 N
대각선 방향으로 움직일 수 있음

대각선 방향으로 움직이고 사각형 모양을 그리며 출발한 카페로 돌아와야함
같은 숫자 x

같이 하나의 카페에서 디저트도 안된다

dfs(좌표, 방문여부, 갯수)

'''
direct = [
    (1,1),
    (1,-1),
    (-1,-1),
    (-1,1),
]

def find_max_value(board):
    N = len(board)
    mx_count = -1
    
    def dfs(x, y, start_x, start_y, direction, count, visited_nums):
        nonlocal mx_count

        for d in range(direction, direction + 2):
            if d >= 4:
                continue
            nx, ny = x + direct[d][0], y + direct[d][1]

            if 0<= nx < N and 0 <= ny < N:
                if nx == start_x and ny == start_y and count >= 4:
                    if nx == start_x and ny == start_y and count >= 4:
                        mx_count = max(mx_count, count)
                        continue

                num = board[nx][ny]
                if num not in visited_nums:
                    visited_nums.add(num)
                    dfs(nx, ny, start_x, start_y, d, count + 1, visited_nums)
                    visited_nums.remove(num)

    for i in range(N):
        for j in range(N):
            dfs(i, j, i,j, 0, 1, {board[i][j]})

    return mx_count

def solution():
    result = 0
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    result = find_max_value(board)

    return result


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
