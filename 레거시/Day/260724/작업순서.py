# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18TrIqIwUCFAZN
from collections import defaultdict, deque


def solution():
    v,e = map(int, input().split())
    lst = list(map(int, input().split()))
    graph = defaultdict(list)
    cnt_node = defaultdict(int)
    
    for i in range(0, e*2, 2):
        a, b = lst[i], lst[i+1]
        graph[a].append(b)
        cnt_node[b] += 1
    
    q = deque()
    for i in range(1, v+1):
        if i not in cnt_node:
            q.append(i)
            cnt_node[i] = 0
    
    answer = []
    while q:
        node = q.popleft()
        answer.append(node)

        for nxt_node in graph[node]:
            cnt_node[nxt_node] -= 1
            if cnt_node[nxt_node] == 0:
                q.append(nxt_node)

    return ' '.join(map(str, answer))

for t in range(1,11):
    print(f'#{t} {solution()}')
