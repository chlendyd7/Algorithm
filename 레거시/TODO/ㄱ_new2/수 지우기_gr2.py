s = list(map(int, input()))
to_delete = list(map(int, input()))

tc = [0] * 10 # total counts
for v in s:
    tc[v] += 1
dc = [0] * 10 # delete counts
for v in to_delete:
    dc[v] += 1
sc = [0] * 10 # save counts
for i in range(10):
    sc[i] = tc[i] - dc[i]

cur = []
for v in s:
    if sc[v]:
        cur.append(v)
        sc[v] -= 1
        
        for i in range(len(cur) - 2, -1, -1):
            if cur[i] < v and dc[cur[i]]:
                dc[cur[i]] -= 1
                sc[cur[i]] += 1
                del cur[i]
            else:
                break
    else:
        dc[v] -= 1
        
print(''.join(map(str, cur)))