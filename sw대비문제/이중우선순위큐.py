from collections import defaultdict, deque


t = int(input())
Q = deque()
for _ in range(t):
    # check=defaultdict(int)
    for i in range(int(input())):
        how, data = input().split()
        data = int(data)
        if how == 'I':
            Q.append(data)
        if Q:
            if how == 'D':
                if data == 1:
                    Q.pop()
                else:
                    Q.popleft()
    Q = list(Q)
    Q.sort()
    Q = deque(Q)
    if Q:
        print("%d %d" %(Q[-1], Q[1]))
    else:
        print("EMPTY")
