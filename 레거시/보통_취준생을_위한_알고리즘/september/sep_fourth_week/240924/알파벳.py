def solution(x,y, count):
    global answer
    answer = max(answer, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < r and 0<= ny < r and lst[nx][ny] not in alpha:
            alpha.add(lst[nx][ny])
            solution(nx,ny,count+1)
            alpha.remove(lst[nx][ny])

r,c = map(int, input().split())
lst = [list(input()) for _ in range(r)]
alpha = set()
dx = [1,0,-1,0]
dy = [0,1,0,-1]
answer = 0
alpha.add(lst[0][0])
solution(0,0,1)
print(answer)