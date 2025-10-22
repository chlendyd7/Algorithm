N,M = map(int, input().split())

stack = []
def backtracking(start, depth):
    if depth == M:
        print(' '.join(map(str, stack)))
        return
    for i in range(start, N+1):
        stack.append(i)
        backtracking(i, depth + 1)
        stack.pop()


backtracking(1, 0)


