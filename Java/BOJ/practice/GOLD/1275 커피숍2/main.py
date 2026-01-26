N, Q = map(int, input().split())
nums = list(map(int, input().split()))
for _ in range(Q):
    x,y,a,b = map(int, input().split())
    result = 0
    for i in range(x, y+1):
        result += nums[i-1]
    print(result)
    nums[a-1] = b

