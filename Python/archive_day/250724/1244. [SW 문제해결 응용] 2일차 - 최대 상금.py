def solution():
    num, chance = input().split()
    num, chance = list(num), int(chance)
    length = len(num)
    
    visited = set()
    max_result = 0
    
    def dfs(depth):
        nonlocal max_result
        key = (''.join(num), depth)
        if key in visited:
            return
        visited.add(key)

        if depth == chance:
            max_result = max(max_result, int(''.join(num)))
            return
        
        for i in range(length):
            for j in range(i+1, length):
                num[i], num[j] = num[j], num[i]
                dfs(depth + 1)
                num[i], num[j] = num[j], num[i]
    
    dfs(0)
    return max_result


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
