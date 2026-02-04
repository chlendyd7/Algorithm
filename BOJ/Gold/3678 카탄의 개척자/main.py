import sys

# 속도를 위해 입력 함수 재정의
input = sys.stdin.readline

def solve():
    # 1. 육각형 6방향 오프셋 정의
    # 순서: ↖, ↗, →, ↘, ↙, ←
    dx = [-1, 1, 2, 1, -1, -2]
    dy = [2, 2, 0, -2, -2, 0]

    ans = [0] * 10001
    board = {} # (x, y) 좌표 -> 자원 번호
    counts = [0] * 6 # 자원(1~5) 누적 사용 횟수

    def place_tile(x, y, idx):
        used_nearby = set()
        for i in range(6):
            nx, ny = x + dx[i], y + dy[i]
            if (nx, ny) in board:
                used_nearby.add(board[(nx, ny)])
        
        best_res = -1
        min_val = 10001
        for res in range(1, 6): # 모든 수가 사용되는 경우는 없을 것 같음
            if res in used_nearby:
                continue
            if counts[res] < min_val:
                min_val = counts[res]
                best_res = res
        
        ans[idx] = best_res
        board[(x, y)] = best_res
        counts[best_res] += 1

    # 초기값 설정
    curr_x, curr_y = 0, 0
    ans[1] = 1
    board[(0, 0)] = 1
    counts[1] = 1
    
    # 10,000번까지 미리 시뮬레이션
    tile_idx = 2
    for layer in range(1, 70):
        if tile_idx > 10000: break
        
        # 층의 시작점 이동
        curr_x += dx[0]
        curr_y += dy[0]
        place_tile(curr_x, curr_y, tile_idx)
        tile_idx += 1
        
        for direction in range(6):
            steps = (layer - 1) if direction == 0 else layer
            move_dir = (direction + 1) % 6
            
            for _ in range(steps):
                if tile_idx > 10000: break
                curr_x += dx[move_dir]
                curr_y += dy[move_dir]
                place_tile(curr_x, curr_y, tile_idx)
                tile_idx += 1

    # 2. 입력 처리 (실시간으로 읽기)
    try:
        line = input().split()
        if not line: return
        num_test_cases = int(line[0])
        
        for _ in range(num_test_cases):
            n_line = input().split()
            if not n_line: break
            n = int(n_line[0])
            print(ans[n])
    except EOFError:
        pass

if __name__ == "__main__":
    solve()