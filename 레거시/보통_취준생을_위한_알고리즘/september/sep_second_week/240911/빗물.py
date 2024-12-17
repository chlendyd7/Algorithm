def solution(H, W, worlds):
    answer = 0
    left = 0
    right = 0
    for i in range(1, W-1):
        left = max(worlds[:i])
        right = max(worlds[i:])
        check = min(left, right)
        
        if worlds[i] < check:
            answer += check - worlds[i]

    return answer

H, W = map(int,input().split())
worlds = list(map(int,input().split()))
print(solution(H, W, worlds))