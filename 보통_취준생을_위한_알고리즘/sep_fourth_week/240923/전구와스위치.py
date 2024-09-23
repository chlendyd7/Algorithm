n = int(input())
off = list(map(bool, map(int, input())))
check = list(map(bool, map(int, input())))

on = off.copy()
on[0] = not on[0]
on[1] = not on[1]

def solution(lights, count):
    for i in range(1, n-1):
        if lights[i-1] != check[i-1]:
            count += 1
            for j in range(i-1, i+2):
                lights[j] = not lights[j]
    
    if lights[n-1] != check[n-1]:
        count += 1
        lights[n-2] = not lights[n-2]
        lights[n-1] = not lights[n-1]
    if lights == check:
        return count
    else: 
        return -1

if off == check:
    print(0)
else:
    count = solution(off, 0)
    if count != -1:
        print(count)
    else:
        count = solution(on, 1)
        print(count if count else -1)
