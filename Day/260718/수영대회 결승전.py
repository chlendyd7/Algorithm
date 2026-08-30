# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AWKaG6_6AGQDFARV
'''
    섬은 1, 소용돌이 2
    소용돌이는 새ㅑㅇ성되고 22초 유지되다 1초동안 잠잠
    한번 통과한 소용돌이 위에서 머물러 있을 수 있다

    시작점, 도착점

    2<=N<=15 15여서 완탐
    
    현재 위치, 시간(%3으로 소용돌이 유무 파악)
    visited로 체크

'''
from collections import deque


def solution():
    n = int(input())
    maze = [list(map(int, input().split())) for _ in range(n)]
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    visitied = [[0] * n for _ in range(n)]
    visitied[start[0]][start[1]] = True
    answer = 10**18

    def dfs(a,b, cnt):
        nonlocal answer
        if cnt >= answer:
            return

        if (a,b) == end:
            answer = min(answer, cnt)
            return

        nxt_step = []
        for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
            nx, ny = a + dx, b + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visitied[nx][ny] and maze[nx][ny] != 1:
                    nxt_step.append((nx,ny))
        
        for nx, ny in nxt_step:
            visitied[nx][ny] = True
            if maze[nx][ny] == 2:
                if cnt%3 == 0:
                    dfs(nx, ny, cnt+3)
                elif cnt%3 == 1:
                    dfs(nx, ny, cnt+2)
                elif cnt%3 == 2:
                    dfs(nx, ny, cnt+1)
            else:
                dfs(nx, ny, cnt+1)
            visitied[nx][ny] = False

    dfs(start[0], start[1], 0)
    return answer

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')

'''
#1 4
#2 10
#3 7

3
5
0 0 0 0 0
0 0 0 1 0
0 0 0 1 0
2 2 1 1 0
0 0 0 0 0
4 0
2 0
6
0 0 0 0 0 0
0 1 1 0 0 0
0 0 0 1 2 0
1 1 0 1 0 1
0 0 0 1 0 1
0 0 0 2 0 1
5 0
2 5
6
0 0 0 0 0 0
0 0 0 0 0 0
1 0 1 1 1 0
1 0 0 0 0 0
1 0 1 1 1 0
0 0 2 0 2 0
5 0
3 5
'''