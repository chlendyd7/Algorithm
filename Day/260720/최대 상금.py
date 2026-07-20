# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15Khn6AN0CFAYD

def solution():
    nums, n = input().split()
    n = int(n)
    nums = list(nums)
    answer = 0
    visited = set()

    def dfs(number, depth):
        nonlocal answer
        if (tuple(number), depth) in visited:
            return
        
        if depth == n:
            answer = max(answer, int(''.join(number)))
            return
        
        visited.add((tuple(number), depth))

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                temp = number[i]
                number[i] = number[j]
                number[j] = temp
                dfs(number, depth+1)
                number[j] = number[i]
                number[i] = temp
    dfs(nums, 0)

    return answer

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
