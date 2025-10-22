def updown():
    up = []
    down = []
    for i in range(1,n+1):
        if r_first[i-1][1][0] > i:
            up.append(i)
        if r_first[i-1][1][0] < i:
            down.append(i)
    for i in range(len(up)):
        for j in range(up[i],r_first[up[i]-1][1][0]):
            result.append((r_first[up[i]-1][0], 'U'))
    down = sorted(down, reverse=True)
    for i in range(len(down)):
        for j in range(r_first[down[i]-1][1][0], down[i]):
            result.append((r_first[down[i]-1][0], 'D'))

def leftright():
    left = []
    right = []
    for i in range(1,n+1):
        if c_first[i-1][1][0] > i:
            left.append(i)
        if c_first[i-1][1][0] < i:
            right.append(i)
    for i in range(len(left)):
        for j in range(left[i], c_first[left[i]-1][1][0]):
            result.append((c_first[left[i]-1][0], 'L'))
    right = sorted(right, reverse=True)
    for i in range(len(right)):
        for j in range(c_first[right[i]-1][1][0], right[i]):
            result.append((c_first[right[i]-1][0], 'R'))

if __name__=='__main__':
    n = int(input())
    r_first = []
    c_first = []
    result = []
    for i in range(1,n+1):
        r, c= map(int, input().split())
        r_first.append((i,(r,c)))
        c_first.append((i,(c,r)))
    r_first = sorted(r_first, key=lambda x: x[1])
    c_first = sorted(c_first, key=lambda x: x[1])
    updown()
    leftright()
    print(len(result))
    for i in range(len(result)):
        print(result[i][0], result[i][1], sep=' ')

'''
import sys

input = sys.stdin.readline

# 입력받기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr = [[i + 1, *arr[i]] for i in range(N)]

# 방향을 저장할 딕셔너리 초기화
directions = {d: [] for d in 'UDLR'}

# 움직임 처리 함수
def move_direction(down, up, index):
    for current_pos, info in enumerate(arr, start=1):
        i, row, col = info
        target_pos = info[index]
        
        # 현재 위치가 목표 위치보다 크면 'down' 방향으로 이동
        if current_pos > target_pos:
            directions[down].extend([[i, down, row, col]] * (current_pos - target_pos))
        # 현재 위치가 목표 위치보다 작으면 'up' 방향으로 이동
        elif current_pos < target_pos:
            directions[up].extend([[i, up, row, col]] * (target_pos - current_pos))

# 행 기준 정렬 후 상/하 이동 처리
arr.sort(key=lambda x: x[1])  # 행 기준 정렬
move_direction('D', 'U', 1)

# 열 기준 정렬 후 좌/우 이동 처리
arr.sort(key=lambda x: x[2])  # 열 기준 정렬
move_direction('R', 'L', 2)

# 결과 합치기 (우측/하방 이동은 역순으로 합치기)
result = []
for direction in 'DR':
    result.extend(reversed(directions[direction]))
for direction in 'UL':
    result.extend(directions[direction])

# 결과 출력
print(len(result))
for entry in result:
    print(entry[0], entry[1])

'''