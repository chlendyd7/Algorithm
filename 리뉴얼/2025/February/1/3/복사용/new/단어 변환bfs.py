from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)])
    visited = set()

    while queue:
        word, depth = queue.popleft()

        if word == target:
            return depth
        
        for next_word in words:
            if next_word not in visited:
                diff_count = sum(1 for a, b in zip(word, next_word) if a != b)
                if diff_count == 1:
                    queue.append((next_word, depth + 1))
                    visited.add(next_word)
    return 0
