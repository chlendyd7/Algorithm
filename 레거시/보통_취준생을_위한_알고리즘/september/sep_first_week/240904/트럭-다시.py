# https://www.acmicpc.net/problem/13335
from collections import deque

def truck_crossing_bridge(n, w, L, trucks):
    bridge = deque([0] * w)
    current_weight = 0
    time = 0
    for truck in trucks:
        while True:
            time += 1
            current_weight -= bridge.popleft()
            if current_weight + truck <= L:
                bridge.append(truck)
                current_weight += truck
                break
            else:
                bridge.append(0)
    time += w
    return time

n,w,L = map(int,input().split())
trucks = list(map(int,input().split()))
print(truck_crossing_bridge(n, w, L, trucks))
