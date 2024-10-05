def solution(R):
    stack = []
    max_len = 0
    for i in range(len(R)):
        if R[i] != 0:
            stack.append(R[i])
        else:
            if stack:
                n = max(stack)
                max_len = max(max_len, n*len(stack))
                stack = [] 
    
    return max_len

R = [0, 2, 1, 1, 0, 4, 1]
print(solution(R))