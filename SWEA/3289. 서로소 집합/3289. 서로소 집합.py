def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a  # 한쪽 루트에 합치기

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    parent = [i for i in range(n+1)]
    ans = []

    for _ in range(m):
        op, a, b = map(int, input().split())
        if op == 0:  # 합집합
            union(a, b)
        else:  # 같은 집합인지 확인
            if find(a) == find(b):
                ans.append("1")
            else:
                ans.append("0")

    print(f"#{tc} {''.join(ans)}")
