def solution(begin, target, words):
    if target not in words:
        return 0
    
    def dfs(word, visited, depth):
        if word == target:
            return depth
        
        min_steps = float('inf')
        for i in range(len(words)):
            if not visited[i]:
                check = sum(1 for j in range(len(word)) if word[j] != words[i][j])
                if check == 1:
                    visited[i] = True
                    steps = dfs(words[i], visited, depth + 1)
                    if steps:
                        min_steps = min(min_steps, steps)
                    visited[i] = False
        return min_steps if min_steps != float('inf') else 0
    
    visited = [False] * len(words)
    return dfs(begin, visited, 0)

    def dfs(word, words, idx):
        word_len = len(word)
        if word == target:
            return idx
        
        if idx == len(words):
            return 0
        
        for i in range(idx, len(words)):
            check = 0
            for j in range(word_len):
                if word[j] != words[i][j]:
                    check += 1
                    if check >= 2:
                        continue
                dfs(words[i], words, idx + 1)


    

    return dfs(begin, words, 0)

print(solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log", "cog"]))