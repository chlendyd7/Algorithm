import sys

# 1. 재귀 깊이 설정 (N이 10만이므로 필수)
sys.setrecursionlimit(200000)
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]

    mid = (start, end) // 2
    tree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid+1, end)
    return tree[node]

def query_sum(node, start, end, left, right):
    if left > end or right < start:
        return 0
    
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return query_sum(node*2, start, mid, left, right) + query_sum(node*2+1, mid+1, end, left, right)

def update(node, start, end, index, val):
    if index < start or index > end:
        return tree[node]
    
    if start == end:
        tree[node] = val
        return tree[node]

    mid = (start + end) // 2
    tree[node] = update(node * 2, start, mid, index, val) + update(node*2+1, mid, end, index, val)
    return tree[node]

n,q = map(int, input().split())
arr = [0] + list(map(int, input().split()))
tree = [0] * (n * 4)

init(1, 1, n)
for _ in range(q):
    x,y,a,b = map(int, input().split())
    
    left, right = min(x,y), max(x,y)
    print(query_sum(1,1, n, left, right))
    
    arr[a] = b
    update(1,1,n,a,b)
