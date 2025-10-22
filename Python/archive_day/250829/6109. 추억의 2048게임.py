def compress(line):
    nums = [x for x in line if x!= 0]
    result = []
    
    i = 0
    while i < len(nums):
        if i + 1 < len(nums) and nums[i] == nums[i+1]:
            result.append(nums[i] * 2)
            i += 2
        else:
            result.append(nums[i])
            i+=1
    
    result.extend([0] * (len(line) - len(result)))
    return result

def move(board, direction):
    N = len(board)

    if direction == 'left':
        return [compress(row) for row in board]
    
    elif direction == 'right':
        return [compress(row[::-1])[::-1] for row in board]
    
    elif direction == 'up':
        new_board = [[0] * N for _ in range(N)]
        