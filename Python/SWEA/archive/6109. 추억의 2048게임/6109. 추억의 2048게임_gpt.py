def compress(line):
    """한 줄(리스트)을 왼쪽으로 이동시킨 결과를 반환"""
    # 1. 0 제거
    nums = [x for x in line if x != 0]
    result = []
    skip = False

    # 2. 같은 숫자 합치기
    i = 0
    while i < len(nums):
        if i + 1 < len(nums) and nums[i] == nums[i+1]:
            result.append(nums[i] * 2)
            i += 2  # 다음 칸은 이미 합쳤으니 건너뜀
        else:
            result.append(nums[i])
            i += 1

    # 3. 길이 맞추기 (뒤를 0으로 채움)
    result.extend([0] * (len(line) - len(result)))
    return result


def move(board, direction):
    N = len(board)

    if direction == "left":
        return [compress(row) for row in board]

    elif direction == "right":
        return [compress(row[::-1])[::-1] for row in board]

    elif direction == "up":
        new_board = [[0]*N for _ in range(N)]
        for col in range(N):
            col_vals = [board[row][col] for row in range(N)]
            compressed = compress(col_vals)
            for row in range(N):
                new_board[row][col] = compressed[row]
        return new_board

    elif direction == "down":
        new_board = [[0]*N for _ in range(N)]
        for col in range(N):
            col_vals = [board[row][col] for row in range(N)][::-1]
            compressed = compress(col_vals)[::-1]
            for row in range(N):
                new_board[row][col] = compressed[row]
        return new_board


# 실행 예시
if __name__ == "__main__":
    T = int(input().strip())
    for t in range(1, T+1):
        N, S = input().split()
        N = int(N)
        board = [list(map(int, input().split())) for _ in range(N)]

        result = move(board, S)

        print(f"#{t}")
        for row in result:
            print(" ".join(map(str, row)))
