N,L,R = map(int,input().split())
population = [list(map(int,input().split())) for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,-1,0,1]
def bfs(x,y):
    

