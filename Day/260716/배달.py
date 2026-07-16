# https://school.programmers.co.kr/learn/courses/30/lessons/12978

'''
    K시간 이하로 배달이 가능한 마을
    1번 마을에 있는 음식점이 K 이하의 시간에 배달이 가능한 마을의 개수를 return 하면 됩니다.
    a, b(1 ≤ a, b ≤ N, a != b)는 도로가 연결하는 두 마을의 번호이며, c(1 ≤ c ≤ 10,000, c는 자연수)는 도로를 지나는데 걸리는 시간입니다.
    
    
'''

'''
    K시간 이하로 배달이 가능한 마을
    1번 마을에 있는 음식점이 K 이하의 시간에 배달이 가능한 마을의 개수를 return 하면 됩니다.
    a, b(1 ≤ a, b ≤ N, a != b)는 도로가 연결하는 두 마을의 번호이며, c(1 ≤ c ≤ 10,000, c는 자연수)는 도로를 지나는데 걸리는 시간입니다.
    
    
'''
from collections import defaultdict
import heapq
def solution(N, road, K):
    graph = defaultdict(list)
    for a,b,w in road:
        graph[a].append((b,w))
        graph[b].append((a,w))
    
    dist = [10**18] * (N+1)
    dist[1] = 0
    hq = [(0,1)]

    while hq:
        w, node = heapq.heappop(hq)
        if dist[node] < w:
            continue

        for nxt, n_w in graph[node]:
            next_weight = w + n_w
            if dist[nxt] > next_weight:
                dist[nxt] = next_weight
                heapq.heappush(hq, (next_weight, nxt))

    return sum(1 for d in dist if d <= K)




print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))
