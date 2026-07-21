# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18TrIqIwUCFAZN


from collections import defaultdict, deque


def solution():
    v,e = map(int, input().split())
    nodes = list(map(int, input().split()))
    parents = defaultdict(list)
    in_degrees = defaultdict(int)
    nums = set()

    for i in range(0, e*2, 2):
        if nodes[i+1] not in parents[nodes[i]]:
            parents[nodes[i]].append(nodes[i+1])
            in_degrees[nodes[i+1]] += 1
        nums.add(nodes[i])
        nums.add(nodes[i+1])

    q = deque()
    for n in range(1, v+1):
        if n not in in_degrees:
            in_degrees[n] = 0
            q.append(n)
    
    answer = []
    while q:
        node = q.popleft()
        answer.append(node)

        for child in parents[node]:
            in_degrees[child] -= 1
            if in_degrees[child] == 0:
                q.append(child)


    return ' '.join(map(str, answer))

# T = int(input())
for t in range(1, 11):
    print(f'#{t} {solution()}')
