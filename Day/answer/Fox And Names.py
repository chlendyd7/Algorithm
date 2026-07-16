from collections import defaultdict, deque

def solve():
    n = int(input())
    names = [input().strip() for _ in range(n)]
    
    # 그래프와 in-degree 초기화
    graph = defaultdict(set)
    in_degree = defaultdict(int)
    chars = set()
    
    # 모든 문자 수집
    for name in names:
        for c in name:
            chars.add(c)
    
    # 제약 조건 추출
    for i in range(n - 1):
        word1, word2 = names[i], names[i + 1]
        min_len = min(len(word1), len(word2))
        
        found = False
        for j in range(min_len):
            if word1[j] != word2[j]:
                if word2[j] not in graph[word1[j]]:
                    graph[word1[j]].add(word2[j])
                    in_degree[word2[j]] += 1
                found = True
                break
        
        # word2가 word1의 접두사인데 word1이 앞에 있으면 불가능
        if not found and len(word1) > len(word2):
            print("Impossible")
            return
    
    # in_degree 초기화
    for c in chars:
        if c not in in_degree:
            in_degree[c] = 0
    
    # Kahn의 알고리즘 (위상 정렬)
    queue = deque([c for c in sorted(chars) if in_degree[c] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in sorted(graph[node]):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # 사이클 확인
    if len(result) != len(chars):
        print("Impossible")
        return
    
    # 나머지 26글자 추가
    for c in 'abcdefghijklmnopqrstuvwxyz':
        if c not in chars:
            result.append(c)
    
    print(''.join(result))

solve()
