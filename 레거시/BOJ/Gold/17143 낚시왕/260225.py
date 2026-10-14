R,C,M = map(int, input().split())
sharks = {}
for _ in range(M):
    r,c,s,d,z = map(int, input().split())
    if d in (1,2):
        if R > 1: s %= (2 * R -2)
    else:
        if C > 1: s %= (2 * C - 2)
    sharks[(r-1,c-1)] = (s,d,z)
direction = [(0,0), (-1,0), (1,0), (0,1), (0,-1)]
def move_sharks(current_sharks):
    new_sharks = {}
    
    for (r,c), (s, d, z) in current_sharks.items():
        c_r, c_c, c_d = r, c, d
    
        for _ in range(s):
            dr, dc = direction[c_d]
            nr, nc = c_r + dr, c_c + dc
            
            if not (0 <= nr < R and 0 <= nc < C):
                if curr_d == 1: curr_d = 2
                elif curr_d == 2: curr_d = 1
                elif curr_d == 3: curr_d = 4
                elif curr_d == 4: curr_d = 3
                
                dr, dc = direction[curr_d]
                nr, nc = c_r + dr, c_c + dc
        
        c_r, c_c = nr, nc
    
    if (curr_r, curr_c) in new_sharks:
            # 기존 상어보다 내가 더 크면 덮어쓰기
            if z > new_sharks[(curr_r, curr_c)][2]:
                new_sharks[(curr_r, curr_c)] = [s, curr_d, z]
        else:
            new_sharks[(curr_r, curr_c)] = [s, curr_d, z]
            
    return new_sharks

total_catch = 0
for people_c in range(C):
    target_r = -1
    for r in range(R):
        if (r, people_c) in sharks:
            target_r = r
            break
    if target_r != -1:
        total_catch += sharks[(target_r, people_c)][2]
        del sharks[(target_r, people_c)]
    
    sharks = move_sharks(sharks)
print(total_catch)
