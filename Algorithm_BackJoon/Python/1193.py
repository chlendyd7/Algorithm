N = int(input())
cnt = 1
first = 1
second = 1
for i in range(N):
    if first < cnt:
        second +=1
        first -=1
    
    elif second < cnt:
        first +=1
        second -=1
    else: