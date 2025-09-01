'''
    K개의 미생물 군집
    N * N 개의 정사각형 셀
    바깥자리 특수약품
    격리시간 M
    M 시간 후 남아 있는 미생물 수의 총 합

'''
direction = {
    'U': (-1,0),
    'D': (1,0),
    'L': (0,-1),
    'R': (0,1),
}
REVERSE = {
    'U':'D',
    'D':'U',
    'L':'R',
    'R':'L'
}
CONVERT = {
    1:'U',
    4:'R',
    3:'L',
    2:'D'
}
tbl = [0, 2, 1, 4, 3]
di = [0,-1,1,0,0]
dj = [0,0,0,-1,1]

def solution():
    N,M,K = map(int,input().split())
    grid = [[0] * N for _ in range(N)]
    arr = [list(map(int, input().split())) for _ in range(K)]
    for _ in range(M):
        for i in range(len(arr)):
            arr[i][0] = arr[i][0] + di[arr[i][3]]
            arr[i][1] = arr[i][1] + dj[arr[i][3]]
            if arr[i][0] == 0 or arr[i][0] == N-1 or arr[i][1] == 0 or arr[i][1] == N-1:
                arr[i][2] //=2
                arr[i][3] = tbl[arr[i][3]]
        
        arr.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)
        i = 1
        while i < len(arr):
            if arr[i-1][0:2] == arr[i][0:2]:
                arr[i-1][2] += arr[i][2]
                arr.pop(i)
            else:
                i += 1
    ans = 0
    for lst in arr:
        ans += lst[2]

    return ans


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')