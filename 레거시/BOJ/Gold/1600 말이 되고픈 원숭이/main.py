from collections import deque


k = int(input())
w,h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]
visited = [[[-1] * (k+1) for _ in range(w)] for _ in range(h)]

def check(r, c, cnt):
    if 0<= r < h and 0<= c < w and \
        visited[r][c][cnt] == -1 and not board[r][c]:
            return True
    return False


direction = [(0,1), (1,0), (-1,0), (0,-1)]
hourse = [(2,1), (2,-1), (1,2), (-1,2), (-2,1), (-2,-1), (1,-2), (-1,-2)]

q = deque([(0,0,k)])
visited[0][0][k] = 0

while q:
    r,c,cnt = q.popleft()

    if r==h-1 and c==w-1:
        print(visited[r][c][cnt])
        break

    if cnt:
        for rr, cc in hourse:
            nr, nc = r + rr, c + cc
            if check(nr, nc, cnt):
                q.append((nr,nc,cnt-1))
                visited[nr][nc][cnt-1] = visited[r][c][cnt] + 1

    for rr, cc in direction:
        nr, nc = r+rr, c+cc
        if check(nr,nc,cnt):
            q.append((nr,nc,cnt))
            visited[nr][nc][cnt] = visited[r][c][cnt] + 1

