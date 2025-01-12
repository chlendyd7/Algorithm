def solution(n):
    triangle = [[0] * (i + 1) for i in range(n)]
    
    direction = [(1,0), (0,1), (-1,-1)]
    direction_idx = 0
    
    row, col = 0, 0
    num = 1
    max_num = n * (n+1) // 2
    
    while num <= max_num:
        triangle[row][col] = num
        num += 1
        
        dr, dc = direction[direction_idx]
        new_row, new_col = row + dr, col + dc
        
        if not (0 <= new_row < n and 0<= new_col < len(triangle[new_row]) and triangle[new_row][new_col] == 0):
            direction_idx = (direction_idx + 1) % 3
            dr, dc = direction[direction_idx]
        
        row, col = row + dr, col + dc
    
    result = []
    for line in triangle:
        result.extend(line)
    return result
print(solution(4))