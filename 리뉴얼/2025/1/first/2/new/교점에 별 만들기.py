def solution(line):
    points = []
    # 1. 모든 직선 쌍에 대해 교점 계산
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            A1, B1, C1 = line[i]
            A2, B2, C2 = line[j]
            denominator = A1 * B2 - A2 * B1
            if denominator == 0:
                continue  # 평행한 경우
            x = (B1 * C2 - B2 * C1) / denominator
            y = (A2 * C1 - A1 * C2) / denominator
            if x.is_integer() and y.is_integer():
                points.append((int(x), int(y)))
    
    # 2. 좌표 범위 계산
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)
    
    # 3. 별 그리기
    grid = [['.' for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
    for x, y in points:
        grid[max_y - y][x - min_x] = '*'
    
    return [''.join(row) for row in grid]
