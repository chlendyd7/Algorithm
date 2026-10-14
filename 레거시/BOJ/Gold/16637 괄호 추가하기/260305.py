def calculate(n1, op, n2):
    """기본 연산 수행 함수"""
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2

def dfs(idx, curr):
    global mx
    
    if idx >= len(ops):
        mx = max(mx, curr)
        return
    
    dfs(idx+1, calculate(curr, ops[idx], nums[idx+1]))
    
    if idx+1 < len(ops):
        bracket_val = calculate(nums[idx+1], ops[idx+1], nums[idx+2])
        dfs(idx+2, calculate(curr, ops[idx], bracket_val))


N = int(input())
nums = []
ops = []
inputs = input()
for i in range(N):
    if i%2 == 0:
        nums.append(int(inputs[i]))
    else:
        ops.append(inputs[i])

mx = -float('inf')
dfs(0, nums[0])
print(mx)