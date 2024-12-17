n,c = map(int,input().split())
lst = [int(input().rstrip()) for _ in range(n)]
lst.sort()
lt, rt = 1, lst[-1] - lst[0] #최소 사이 거리 1
result = 0

while lt <= rt:
    mid = (lt + rt) // 2  # 현재 검사하는 두 공유기 사이의 거리(mid)
    now = 0                    # 현재 공유기가 설치된 인덱스(첫 번째 지점에 설치)
    cnt = 1                    # 첫 번째 공유기는 항상 설치된다고 가정하므로 1로 시작
    for i in range(n):
        if lst[i] - lst[now] >= mid:
            now = i
            cnt += 1
    if cnt >= c:
        lt = mid + 1
        result = mid
    else:
        rt = mid - 1
print(result)
