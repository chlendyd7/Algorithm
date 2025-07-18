T = int(input())
for i in range(1, T+1):
    N = float(input())
    result = []
    flag = True
    while N > 0:
        if len(result) >= 12:
            flag = False
            break
        
        N *= 2
        if N >= 1:
            result.append('1')
            N -= 1
        else:
            result.append('0')
    
    if flag:
        print(f'#{i} ' + ''.join(result))
    else:
        print(f'#{i} overflow')
