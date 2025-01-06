def solution(n, left, right):
    result = []
    
    for k in range(left, right + 1):
        row = k // n  # 행 번호
        col = k % n   # 열 번호
        result.append(max(row + 1, col + 1))
    
    return result