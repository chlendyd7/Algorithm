from collections import deque
def solution(priorities, location):
    q = deque()
    for i in range(len(priorities)):
        q.append((priorities[i],i))
    
    cnt = 0
    while q:
        mx = max(q)[0]
        now = q.popleft()
        print(mx, now)
        if max == now[0]:
            cnt += 1
            if now[1] == location:
                return cnt
            else:
                cnt
        else:
            q.append(now)
            
    
    return answer