import heapq
def solution(k, score):
    answer = []
    h = []
    i = 0
    for i in range(k):
        heapq.heappush(h, score[i])
        answer.append(h[0])
    for i in range(k, len(score)):
        minn = h[0]
        if score[i] >= minn:
            heapq.heappushpop(h, score[i])
        answer.append(h[0])
    return answer
