board = [list(map(int, input().split())) for _ in range(10)]
ones = [(r,c) for r in range(10) for c in range(10) if board[r][c]==1]
papers = [0,5,5,5,5,5]
min_val = 26

def solve(idx, cnt):
    global min_val
    if cnt >= min_val:
        return
    
    r,c = ones[idx]
    if board[r][c] == 0:
        solve(idx+1, cnt)
        return
    for size in range(5, 0, -1):
        if papers[size] > 0 and r + size <= 10 and c + size <= 10:
            if all(board[nr][nc] for nr in range(r, r+size) for nc in range(c, c+size)):
                for nr in range(r, r+size):
                    for nc in range(c, c+size):
                        board[nr][nc] = 0
                papers[size] -= 1
                
                solve(idx+1, cnt+1)
                papers[size] +=1
                for nr in range(r, r+size):
                    for nc in range(c, c+size):
                        board[nr][nc] = 1
solve(0, 0)
print(min_val if min_val != 26 else -1)
