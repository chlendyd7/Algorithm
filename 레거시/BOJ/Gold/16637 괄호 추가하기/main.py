import sys
import os

# 로컬에서 테스트할 때만 주석 해제
# current_dir = os.path.dirname(os.path.abspath(__file__))
# sys.stdin = open(os.path.join(current_dir, 'input.txt'), 'r')
# sys.stdout = open(os.path.join(current_dir, 'output.txt'), 'w')

input = sys.stdin.readline

def calculate(n1, op, n2):
    """기본 연산 수행 함수"""
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2

def dfs(idx, current_val):
    global max_res
    
    if idx >= len(ops):
        max_res = max(max_res, current_val)
        return

    next_val = calculate(current_val, ops[idx], nums[idx+1])
    dfs(idx+1, next_val)

    if idx+1 < len(ops):
        bracket_val = calculate(nums[idx+1], ops[idx+1], nums[idx+2])
        next_val_with_bracket = calculate(current_val, ops[idx], bracket_val)
        dfs(idx+2, next_val_with_bracket)




N = int(input())
expression = input()
nums = []
ops = []

for i in range(N):
    if i%2 == 0:
        nums.append(int(expression[i]))
    else:
        ops.append(expression[i])

max_res = -float('inf')

dfs(0, nums[0])
print(max_res)