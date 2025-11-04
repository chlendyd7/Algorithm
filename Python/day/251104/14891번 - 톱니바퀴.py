gears = [list(map(int, input().strip())) for _ in range(4)]
K = int(input())

for _ in range(K):
    idx, direction = map(int, input().split())
    idx -= 1

    rotate_dir = [0] * 4
    rotate_dir[idx] = direction

    