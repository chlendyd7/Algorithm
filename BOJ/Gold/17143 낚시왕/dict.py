import sys
input = sys.stdin.readline

# 방향: 1(위), 2(아래), 3(우), 4(좌)
direction = [(0,0), (-1,0), (1,0), (0,1), (0,-1)]

R, C, M = map(int, input().split())
# sharks 딕셔너리: {(r, c): [s, d, z]}
sharks = {}

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    # 사용자님의 주기 최적화 아이디어
    if d in (1, 2):
        if R > 1: s %= (2 * R - 2)
    else:
        if C > 1: s %= (2 * C - 2)
    sharks[(r-1, c-1)] = [s, d, z]

def move_sharks(current_sharks):
    new_sharks = {} # 이동 후 상어들을 담을 딕셔너리
    
    for (r, c), (s, d, z) in current_sharks.items():
        curr_r, curr_c, curr_d = r, c, d
        
        # s만큼 실제로 이동 (벽 충돌 처리)
        for _ in range(s):
            dr, dc = direction[curr_d]
            nr, nc = curr_r + dr, curr_c + dc
            
            if not (0 <= nr < R and 0 <= nc < C):
                # 방향 전환: 1<->2, 3<->4
                if curr_d == 1: curr_d = 2
                elif curr_d == 2: curr_d = 1
                elif curr_d == 3: curr_d = 4
                elif curr_d == 4: curr_d = 3
                
                dr, dc = direction[curr_d]
                nr, nc = curr_r + dr, curr_c + dc
            
            curr_r, curr_c = nr, nc
        
        # 이동 후 위치(curr_r, curr_c)에서 크기 비교
        if (curr_r, curr_c) in new_sharks:
            # 기존 상어보다 내가 더 크면 덮어쓰기
            if z > new_sharks[(curr_r, curr_c)][2]:
                new_sharks[(curr_r, curr_c)] = [s, curr_d, z]
        else:
            new_sharks[(curr_r, curr_c)] = [s, curr_d, z]
            
    return new_sharks

total_catch = 0
for people_c in range(C):
    # 1. 가장 가까운 상어 잡기
    # 해당 열(people_c)에 있는 상어들 중 행(r)이 가장 작은 것 찾기
    target_r = -1
    for r in range(R):
        if (r, people_c) in sharks:
            target_r = r
            break
            
    if target_r != -1:
        total_catch += sharks[(target_r, people_c)][2]
        del sharks[(target_r, people_c)] # 딕셔너리에서 제거
        
    # 2. 상어 이동
    sharks = move_sharks(sharks)

print(total_catch)