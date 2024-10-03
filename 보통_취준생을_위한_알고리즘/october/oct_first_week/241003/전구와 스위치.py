

def check(bulb, count):
    for i in range(1, n-1):
        if bulb[i-1] != target[i-1]:
            count += 1
            for j in range(i-1, i+2):
                bulb[j] = not bulb[j]
    
    if bulb[n-1] != target[n-1]:
        count += 1
        bulb[n-1] = not bulb[n-1]
        bulb[n-2] = not bulb[n-2]
    
    if bulb == target:
        return count
    else:
        return -1






n = int(input())
off = list(map(int, input()))
target = list(map(int, input()))
on = off.copy()
on[0] = not on[0]
on[1] = not on[1]

if check(off, 0) == -1:
    print(check(on, 1))
else:
    print(check(off, 0))
