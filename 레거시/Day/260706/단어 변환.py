def solution(begin, target, words):
    def check(first, second):
        cnt = 0
        for i in range(len(first)):
            if first[i] != second[i]:
                cnt += 1
            if cnt > 1:
                return False
        return True
    
    def dfs(word, n, visited):
        nonlocal answer
        if word == target:
            answer = min(answer, n)
        
        for w in words:
            if word != w and check(word, w) and w not in visited:
                visited.append(w)
                dfs(w, n+1, visited)
                visited.pop()

    answer = 1e9
    dfs(begin, 0, [begin])

    return answer if answer != 1e9 else 0

from collections import deque

def solution(begin, target, words):
    # target이 words 안에 없으면 절대 변환할 수 없으므로 바로 0 반환
    if target not in words:
        return 0
        
    def check(first, second):
        cnt = 0
        for i in range(len(first)):
            if first[i] != second[i]:
                cnt += 1
            if cnt > 1:
                return False
        return True

    # 큐에는 (현재 단어, 이동 횟수)를 담습니다.
    queue = deque([(begin, 0)])
    visited = set([begin]) # 탐색 속도를 위해 set 사용

    while queue:
        current_word, steps = queue.popleft()
        
        # 목표 단어에 도달하면 즉시 현재까지의 단계를 반환 (가장 먼저 도달한 것이 최단 거리)
        if current_word == target:
            return steps
            
        for w in words:
            if w not in visited and check(current_word, w):
                visited.add(w)
                queue.append((w, steps + 1))
                
    return 0



from collections import deque

def solution(begin, target, words):
    # 예외 처리: target이 words에 없으면 변환 불가능
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)])
    visited = set([begin])
    
    while queue:
        current, steps = queue.popleft()
        
        # 목표 단어에 도달하면 즉시 횟수 반환
        if current == target:
            return steps
            
        for word in words:
            if word not in visited:
                # zip을 활용해 정석적으로 한 글자만 다른지 체크
                diff_count = sum(1 for a, b in zip(current, word) if a != b)
                
                if diff_count == 1:
                    visited.add(word)
                    queue.append((word, steps + 1))
                    
    return 0