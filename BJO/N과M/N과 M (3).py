N,M = map(int, input().split())

stack = []
def backtracking(depth):
    if depth == M:
        print(' '.join(map(str, stack)))
        return
    for i in range(1, N+1):
        stack.append(i)
        backtracking(depth + 1)
        stack.pop()


backtracking(0)

