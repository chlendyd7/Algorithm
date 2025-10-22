def solution(mats, park):
    def can_place_mat(mat_size, start_row, start_col):
        """매트를 특정 위치에 배치할 수 있는지 확인."""
        for i in range(start_row, start_row + mat_size):
            for j in range(start_col, start_col + mat_size):
                if park[i][j] != "-1":
                    return False
        return True

    rows, cols = len(park), len(park[0])
    mats.sort(reverse=True)  # 매트 크기를 큰 순서대로 정렬

    for mat_size in mats:
        for i in range(rows - mat_size + 1):
            for j in range(cols - mat_size + 1):
                if can_place_mat(mat_size, i, j):
                    return mat_size  # 가장 큰 매트를 찾으면 바로 반환

    return -1  # 배치 가능한 매트가 없을 경우