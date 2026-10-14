# https://codeforces.com/problemset/problem/510/C
from collections import defaultdict, deque


def solve():
    n = int(input())
    names = [input() for _ in range(n)]
    chars = set()
    degree = defaultdict(list)
    in_degree = defaultdict(int)
    # 모든 문자 수집
    for name in names:
        for n in name:
            chars.add(n)
    
    # 제약 조건 추출
    for i in range(n-1):
        name1 = names[i]
        name2 = names[i+1]

        check = False
        min_len = min(len(name1), len(name2))
        for j in range(min_len):
            if name1[j] != name2[j]:
                if name2[j] not in degree[name1[j]]:
                    degree[name1[j]].append(name2[j])
                    in_degree[name2[j]] += 1
                check=True
                break
        
        # word2가 word1의 접두사인데 word1이 앞에 있으면 불가능
        if not check and len(name1) > len(name2):
            print("Impossible")
            return

    # in_degree 초기화
    for c in chars:
        if c not in in_degree:
            in_degree[c] = 0

    queue = deque([c for c in sorted(chars) if in_degree[c] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in sorted(degree[node]):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    if len(result) != len(chars):
        print("Impossible")
        return
    
    for c in "abcdefghijklmnopqrstuvwxyz":
        if c not in chars:
            result.append(c)
    
    print(''.join(result))

solve()