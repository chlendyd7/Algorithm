def solution(wallpaper):
    max_row, max_col = float('-inf'), float('-inf')
    min_row, min_col = float('inf'), float('inf')
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                min_row = min(min_row, i)
                min_col = min(min_col, j)
                max_row = max(max_row, i)
                max_col = max(max_col, j)

    return [min_row, min_col, max_row + 1, max_col + 1]