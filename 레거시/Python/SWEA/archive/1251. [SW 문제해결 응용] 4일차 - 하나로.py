from heapq import heappop, heappush


def solution():
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    pq = []
    for i in range(N):
        for j in range(i+1, N):
            heappush(pq, (E * ((abs(X[i] - X[j]) ** 2 + abs(Y[i] - Y[j]) ** 2) ** 0.5) ** 2, i, j))
    parent = [i for i in range(N)]

    while pq:
        cost, start, end = heappop(pq)

        if parent.count(0) == N:
            break
        if find(start) != find(end):
            ans += cost
            union(start, end)


    def find(value):
        if parent[value] != value:
            parent[value] = find(parent[value])
        return parent[value]

    def union(A, B):
        A = find(A)
        B = find(B)
        
        if A < B:
            parent[B] = A
        else:
            parent[A] = B



    return


T = int(input())
for t in range(1, T+1):
    N = int(input())
    x_array = list(map(int, input().split()))
    y_array = list(map(int, input().split()))
    E = float(input())
    
    print(f'#{t} {solution()}')