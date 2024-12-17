def solution(bulbs, count):
    for i in range(1, n-1):
        if bulbs[i-1] != target[i-1]:
            count += 1
            for j in range(i-1, i+2):
                bulbs[j] = not bulbs[j]
    
    if bulbs[n-1] != target[n-1]:
        count += 1
        bulbs[n-1] = not bulbs[n-1]
        bulbs[n-2] = not bulbs[n-2]
    
    if bulbs == target:
        return count
    else:
        return -1



n = int(input())
off = list(map(bool, map(int, input())))
target = list(map(bool, map(int, input())))

on = off.copy()
on[0] = not on[0]
on[1] = not on[1]
print(solution(off,0))
if solution(off,0) == -1:
    print(solution(on,1))
else:
    print(solution(off, 0))
