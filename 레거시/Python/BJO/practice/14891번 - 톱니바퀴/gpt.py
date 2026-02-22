gears = [list(map(int, input().strip())) for _ in range(4)]
K = int(input())

def rotate(gear, direction):
    if direction == 1:
        gear.insert(0, gear.pop())
    else:
        gear.append(gear.pop(0))


for _ in range(K):
    idx, direction = map(int, input().split())
    idx -= 1

    rotate_dir = [0] * 4
    rotate_dir[idx] = direction

    for i in range(idx -1, -1, -1):
        if gears[i][2] != gears[i+1][6]:
            rotate_dir[i] = -rotate_dir[i+1]
        else:
            break
    
    for i in range(idx + 1, 4):
        if gears[i-1][2] != gears[i][6]:
            rotate_dir[i] = - rotate_dir[i-1]
        else:
            break

    for i in range(4):
        if rotate_dir[i] != 0:
            rotate(gears[i], rotate_dir[i])

score = 0
for i in range(4):
    if gears[i][0] == 1:
        score += (1 << i)

print(score)
