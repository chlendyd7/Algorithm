def prim(start):
    global result
    dist_array[start]
    return


T = int(input())
for t in range(1, T+1):
    N = int(input())
    x_array = list(map(int, input().split()))
    y_array = list(map(int, input().split()))
    E = float(input())
    
    visited = [0] * N
    dist_array = [float('inf')] * N
    result = 0
    prim(0)
