from collections import deque


n,w,l = map(int,input().split())
trucks = deque(list(map(int,input().split())))
line =  deque([0]*w)

line_sum = 0
time = 0

while trucks:
    time += 1
    line_sum -= line.popleft()
    truck = trucks[0]
    if truck + line_sum <= l:
        line_sum += truck
        line.append(trucks.popleft())
    else:
        line.append(0)
print(time+w)