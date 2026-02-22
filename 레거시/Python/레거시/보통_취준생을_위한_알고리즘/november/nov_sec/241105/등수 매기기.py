n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort()
answer = 0
for i in range(n):
    answer += abs((i+1)-lst[i])
print(answer)

# 입력 처리
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
predicted_ranks = list(map(int, data[1:]))

# 예상 등수를 오름차순 정렬
predicted_ranks.sort()

# 최소 불만족도 계산
dissatisfaction = 0
for i in range(N):
    actual_rank = i + 1
    dissatisfaction += abs(predicted_ranks[i] - actual_rank)

print(dissatisfaction)
