from collections import defaultdict, deque

def solve():
    n = int(input())
    names = [input() for _ in range(n)]

    graph = defaultdict(set)
    in_degree = defaultdict(int)
    chars = set()

    for name in names:
        for c in names:
            chars.add(c)

    for i in range(n-1):
        word1, word2 = names[i], names[i+1]
        min_len = min(len(word1), len(word2))
        
        found = False
        for j in range(min_len):
            if word1[j] != word2[j]:
                # 첫 다른 문자 발견!
                if word2[j] not in graph[word1[j]]:
                    graph[word1[j]].add(word2[j])
                    in_degree[word2[j]] += 1
                found = True
                break
        
        if not found and len(word1) > len(word2):
            print("Impossible")
            return

    for c in chars:
        if c not in in_degree:
            in_degree[c] = 0
    
    queue = deque([c for c in sorted(chars) if in_degree[c] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in sorted(graph[node]):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(result) != len(chars):
        print("Impossible")
        return
    
    for c in 'abcdefghijklmnopqrstuvwxyz':
        if c not in chars:
            result.append(c)
    
    print(''.join(result))

solve()