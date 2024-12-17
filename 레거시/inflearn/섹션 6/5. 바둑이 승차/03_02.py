def DFS(L, sum):
    global max
    if sum > c:
        return
    if L == n:
        if sum > max:
            max = sum
    else:
        DFS(L + 1, sum + ls[L])
        DFS(L + 1, sum)


if __name__ == '__main__':
    c, n = map(int, input().split())
    ls = [0] * n
    for i in range(n):
        ls[i] = int(input())
    max = 0
    DFS(0, 0)
    print(max)



