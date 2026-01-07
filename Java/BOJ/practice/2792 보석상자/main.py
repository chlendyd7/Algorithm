# 학생은 항상 같은 생삭의 보석만 가져간다
N, M = map(int, input().split())
gems = []
left, right = 1,0

for i in range(M):
    gems.append(int(input()))
    right = max(right, gems[i])
print(gems)

answer = right

while (left <= right):
    mid = (left + right) // 2
    totalStudent = 0

    for gem in gems:
        totalStudent += (gem // mid)
        if gem % mid:
            totalStudent += 1
    
    if totalStudent <= N:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
