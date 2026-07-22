# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LuHfqDz8DFAXc
def solution():
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    print(lst)
    answer = 0
    check = [False] * n
    def dfs(depth, cnt):
        nonlocal answer
        if depth == n:
            answer = max(answer, round(cnt*100, 6))
            return

        for i in range(n):
            if not check[i]:
                check[i] = True
                dfs(depth+1, cnt * lst[depth][i] * 0.01)
                check[i] = False

    dfs(0, 1)
    return (f'{answer:.6f}')

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
