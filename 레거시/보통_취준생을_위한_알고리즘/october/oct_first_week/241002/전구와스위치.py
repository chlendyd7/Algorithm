def gridy(bulbs, cnt=0):
    for i in range(1, n-1):
        if bulbs[i-1] != target[i-1]:
            cnt += 1
            for j in range(i-1, i+2):
                bulbs[j] = not bulbs[j]

    if bulbs[n-1] != target[n-1]:
        cnt += 1
        bulbs[n-2] = not bulbs[n-2]
        bulbs[n-1] = not bulbs[n-1]
    
    if bulbs == target:
        return cnt
    else:
        return -1
n = int(input())
off = list(map(bool, map(int, input())))
target = list(map(bool, map(int, input())))

on = off.copy()
on[0] = not on[0]
on[1] = not on[1]

if off == target:
    print(0)
else:
    #else 부분 틀림 다시 확인
    count = gridy(off, 0)
    if gridy(off) == -1:
        print(gridy(on, 1))
    else:
        print(gridy(off))
