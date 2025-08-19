# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWAe7XSKfUUDFAUw
from itertools import permutations

T = int(input())
# T = 1
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))


    def dfs(left, right, depth, p):
        global answer, total

        if depth == N:
            answer += 1
            return

        now = p[depth]
        
        # “왼쪽 무게가 전체 무게의 절반보다 크다”
        # 남은 추를 오른쪽에 다 올려도 됨 남은 재귀 계산 필요 x
        if left > (total // 2):
            answer += 2 ** (N - depth)
            return

        elif left >= (right + now):
            dfs(left, right + now, depth + 1, p)
            dfs(left + now, right, depth + 1, p)
        else:
            dfs(left + now, right, depth + 1, p)


    answer = 0
    total = sum(numbers)
    for perm in permutations(numbers, N):
        dfs(0, 0, 0, perm)

    print(f"#{test_case} {answer}")
