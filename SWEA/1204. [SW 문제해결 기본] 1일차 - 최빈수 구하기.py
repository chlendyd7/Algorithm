'''
    최빈수 구하기
    특정 자료에서 가장 여러 번 나타나는 값
'''
from collections import defaultdict

T = int(input())
for _ in range(T):
    case = int(input())
    nums = list(map(int,input().split()))
    dic = defaultdict(int)
    for num in nums:
        dic[num] += 1
    result = max(dic, key=lambda k: (dic[k], k))
    print(f'#{case} {result}')


# import sys
# input = sys.stdin.readline

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     scores = list(map(int, input().split()))
#     freq = {}

#     max_freq = 0
#     mode = 0
#     for s in scores:
#         freq[s] = freq.get(s, 0) + 1
#         if freq[s] > max_freq or (freq[s] == max_freq and s > mode):
#             max_freq = freq[s]
#             mode = s

#     print(f"#{tc} {mode}")
