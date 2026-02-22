'''
    가장 큰 자리수부터 작은 자리수까지 감소
    N 번째 감소하는 수
'''

N = int(input())
nums = []
def dfs(prev_num, prev):

    for i in range(prev -1, -1,-1):
        word = prev_num + str(i)
        nums.append(int(word))
        dfs(word, i)

dfs("", 10)
nums.sort()
if N >= len(nums):
    print(-1)
else:
    print(nums[N])
