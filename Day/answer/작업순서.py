# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18TrIqIwUCFAZN


from collections import defaultdict


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

    for n in nums:
        if n not in in_degrees:
            in_degrees[n] = 0



    return

# T = int(input())
for t in range(1, 11):
    print(f'#{t} {solution()}')
