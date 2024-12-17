# https://www.acmicpc.net/problem/1715

import heapq
n = int(input())

card = list(int(input()) for _ in range(n))
heapq.heapify(card)
answer = 0

while len(card) != 1:
    first = heapq.heappop(card)
    scond = heapq.heappop(card)
    sum = first + scond
    answer += sum
    heapq.heappush(card, sum)

print(answer)
