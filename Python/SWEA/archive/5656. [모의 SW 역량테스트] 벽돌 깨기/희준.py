from collections import deque
# 델타값
dr = [0,0,1,-1]
dc = [1,-1,0,0]
 
# BFS 사용
def break_block(cnt, remains, now_arr):
    global min_block
    # 종료 조건
    if cnt == N or remains == 0:
        min_block = min(min_block, remains)
        return
     
    # 깨트릴 곳을 찾아보기
    for col in range(W):
        copy_arr = [row[:] for row in now_arr]
        row = -1
        # 가장 위쪽 찾기
        for i in range(H):
            if copy_arr[i][col]:
                row = i
                break
        # 열에 벽돌이 없을 경우
        if row == -1:
            continue
 
        # BFS
        queue = deque()
        queue.append((row, col, copy_arr[row][col]))
        # 벽돌깨주기
        copy_arr[row][col] = 0
        now_remain = remains - 1
 
        # BFS 반복
        while queue:
            r, c, p = queue.popleft()
            for k in range(1, p):
                for dir in range(4):
                    nr, nc = r + dr[dir]*k, c + dc[dir]*k
                    if 0 <= nr < H and 0 <= nc < W and copy_arr[nr][nc] != 0:
                        queue.append((nr, nc, copy_arr[nr][nc]))
                        copy_arr[nr][nc] = 0
                        now_remain -= 1
         
        # 파괴후 빈칸 메꾸기
        for j in range(W):
            idx = H - 1
            for i in range(H-1, -1, -1):
                if copy_arr[i][j]:
                    copy_arr[i][j], copy_arr[idx][j] = copy_arr[idx][j], copy_arr[i][j]
                    idx -= 1
         
        # 다음번 깨트리기
        break_block(cnt +1, now_remain, copy_arr)
 
T = int(input())
for test_case in range(1, T+1):
    N, W, H = map(int, input().split())
    ground = []
    min_block = W*H
    remain_block = 0
    for i in range(H):
        temp_row = list(map(int, input().split()))
        for j in temp_row:
            if j != 0:
                remain_block += 1
        ground.append(temp_row)    
    break_block(0, remain_block, ground)
    print(f'#{test_case}', min_block)