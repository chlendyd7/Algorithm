n, m = map(int, input().split())
lines = [int(input()) for _ in range(n)]
left, right = 1, max(lines) * m

def check(time): #시간이 들어올꺼고
    temp = 0
    for line in lines:
        temp += time // line
    return temp

result = right
while left <= right:
    mid = (left + right) // 2
    if check(mid) < m:
        left = mid + 1
    else:
        result = min(result, mid)
        right = mid - 1

print(result)

