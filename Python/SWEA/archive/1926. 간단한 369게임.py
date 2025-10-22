def solution(n):
    nums = ["3", "6", "9"]
    result = []
    for i in range(1, n+1):
        str_i = str(i)
        tmp = []
        flag = False
        for c in str_i:
            if c in nums:
                tmp.append('-')
                flag = True
        if flag:
            result.append((''.join(tmp)))
        else:
            result.append(i)
    return result

n = int(input())
print(' '.join(map(str, solution(n))))
