import os
import sys


BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 현재 실행 중인 파일의 절대 경로
sys.stdin = open(os.path.join(BASE_DIR, 'input.txt'), 'r')


def solution():
    N = int(input())
    plus, minus, mul, div = map(int, input().split())
    nums = list(map(int, input().split()))
    print(plus,minus)
    mx, mn = 0, 1e9
    def dfs(n, result, plus, minus, mul, div):
        nonlocal mx, mn

        if n == N:
            mn = min(mn, result)
            mx = max(mx, result)
            return

        if plus:
            dfs(n+1, result + nums[n], plus-1, minus, mul, div)
        if minus:
            dfs(n+1, result - nums[n], plus, minus-1, mul, div)
        if mul:
            dfs(n+1, result * nums[n], plus, minus, mul-1, div)
        if div:
            dfs(n+1, int(result / nums[n]), plus, minus, mul, div-1)
    
    dfs(0, 0, plus, minus, mul, div)
    print(mx, mn)
    return


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')