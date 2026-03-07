def calculate(n1, op, n2):
    """기본 연산 수행 함수"""
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2


N = int(input())
nums = []
giho = []
inputs = list(input())
nums.append(int(inputs[0]))
for i in range(1, N, 2):
    giho.append(inputs[i])
    nums.append(int(inputs[i+1]))
print(giho, nums)

# index를 가지고 있으면서 길이를 체크하면서 나 말고 다음 값들을 묶기
# i가 0부터 시작한다면 
mx = -float('inf')
def dfs(i, cnt):
    global mx
    if i == N//2:
        mx = max(mx, cnt)
        return
    # 3 + 8
    # i가 0 일 때
    # cnt + 8
    # cnt * 7
    # 3 + 8 값이 그 다음으로 들어가야하는데
    # 3 + 8
    print(i+1, cnt, giho[i], nums[i+1])
    dfs(i+1, calculate(cnt, giho[i], nums[i+1]))
cnt = nums[0]
dfs(0, cnt)
