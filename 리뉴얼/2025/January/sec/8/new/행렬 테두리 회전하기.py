def solution(rows, columns, queries):
    # 1. 초기 행렬 생성
    matrix = [[(i * columns + j + 1) for j in range(columns)] for i in range(rows)]
    answer = []

    for query in queries:
        # 2. 쿼리의 좌표 정보 가져오기 (1-based -> 0-based)
        x1, y1, x2, y2 = [q - 1 for q in query]
        
        # 3. 테두리 회전 수행
        temp = matrix[x1][y1]  # 회전 시 첫 값
        min_value = temp
        
        # 왼쪽 세로줄
        for i in range(x1, x2):
            matrix[i][y1] = matrix[i + 1][y1]
            min_value = min(min_value, matrix[i][y1])
        
        # 아래 가로줄
        for i in range(y1, y2):
            matrix[x2][i] = matrix[x2][i + 1]
            min_value = min(min_value, matrix[x2][i])
        
        # 오른쪽 세로줄
        for i in range(x2, x1, -1):
            matrix[i][y2] = matrix[i - 1][y2]
            min_value = min(min_value, matrix[i][y2])
        
        # 위 가로줄
        for i in range(y2, y1, -1):
            matrix[x1][i] = matrix[x1][i - 1]
            min_value = min(min_value, matrix[x1][i])
        
        # 마지막 값 반영
        matrix[x1][y1 + 1] = temp
        answer.append(min_value)
    
    return answer
