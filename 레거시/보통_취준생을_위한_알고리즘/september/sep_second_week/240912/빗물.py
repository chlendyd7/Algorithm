h,w = map(int,input().split())
rains = list(map(int,input().split()))
answer = 0
for i in range(1, w-1):
    left = max(rains[:i])
    right = max(rains[i:])
    tmp = min(left, right)

    if rains[i] < tmp:
        answer += tmp - rains[i]

print(answer)
