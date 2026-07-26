# https://school.programmers.co.kr/learn/courses/30/lessons/87391
def solution(n, m, x, y, queries):
    r_min, r_max = x, x
    c_min, c_max = y, y
    for command, dx in reversed(queries):
        if command == 0:
            if c_min != 0: # 감소하다가 벽에 박았으니까 가만히 둬도 됨
                c_min += dx
            c_max = min(m-1, c_max + dx)
        elif command == 1:
            c_min = max(0, c_min - dx)
            if c_max != m-1:
                c_max -= dx
        
        elif command == 2:
            if r_min != 0:
                r_min += dx
            r_max = min(n-1, r_max + dx)
        elif command == 3:
            r_min = max(0, r_min - dx)
            if r_max != n-1:
                r_max -= dx
        
        if r_min > r_max or c_min > c_max:
            return 0
    
    return (r_max - r_min + 1) * (c_max - c_min + 1)