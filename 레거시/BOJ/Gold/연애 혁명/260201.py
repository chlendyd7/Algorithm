n, m = map(int, input().split())
parents = [i for i in range(n+1)]
def find_parents(x):
    if parents[x] != x:
        parents[x] = find_parents(parents[x])
    return parents[x]


def union_parents(a, b):
    p_a = find_parents(a)
    p_b = find_parents(b)
    if p_a < p_b:
        parents[p_b] = p_a
    else:
        parents[p_a] = p_b

edges = []
total_love = 0
maintain_love = 0
for i in range(m):
    a, b, c, d = map(int, input().split())
    total_love += c
    if d == 1:
        if find_parents(a) != find_parents(b):
            union_parents(a, b)
            maintain_love += c
    else:
        edges.append((c, a, b))

edges.sort(key=lambda x: x[0], reverse=True)
for c, a, b in edges:
    if find_parents(a) != find_parents(b):
        maintain_love += c
        union_parents(a, b)

print(total_love - maintain_love)
