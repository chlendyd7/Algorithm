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
    # 공백 기준으로 자르기 위해 split() 명시적 활용
    pool = [list(map(int, input().split())) for _ in range(n)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    
    visited = [[float('inf')] * n for _ in range(n)]
    q = deque([(start_x, start_y, 0)])
    visited[start_x][start_y] = 0
    
    while q:
        x, y, cnt = q.popleft()
        if cnt > visited[x][y]:
            continue
        if x == end_x and y == end_y:
            continue
        
        for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n:
                if pool[nx][ny] == 1:
                    continue
                
                elif pool[nx][ny] == 2:
                    rem = cnt % 3
                    if rem == 0:
                        next_cnt = cnt + 3
                    elif rem == 1:
                        next_cnt = cnt + 2
                    else:
                        next_cnt = cnt + 1
                else:
                    next_cnt = cnt + 1
                
                if next_cnt < visited[nx][ny]:
                    visited[nx][ny] = next_cnt
                    q.append((nx, ny, next_cnt))
    ans = visited[end_x][end_y]
    return ans if ans != float('inf') else -1


T = int(input())
for t in range(1, T + 1):
    print(f"#{t} {solution()}")