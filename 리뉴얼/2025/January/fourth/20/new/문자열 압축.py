def solution(s):
    if len(s) == 1:
        return 1
    
    answer = []

    for i in range(1, len(s) // 2 + 1):
        compressed = ''
        prev = s[:i]
        count = 1

        for j in range(1, len(s), i):
            if prev == s[j:j+i]:
                count += 1
            else:
                compressed += (str(count) if count > 1 else '') + prev
                prev = s[j:j+i]
                count = 1
        
        compressed += (str(count) if count > 1 else '') + prev
        answer.append(len(compressed))
    
    return min(answer)
