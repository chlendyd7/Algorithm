from collections import defaultdict, deque
import heapq

def solution(genres, plays):
    dic = defaultdict(list)
    plays_dic = defaultdict(int)

    for idx, g in enumerate(genres):
        heapq.heappush(dic[g], (-plays[idx], idx))
        plays_dic[g] += plays[idx]
    
    genres_rank = []
    for g in plays_dic:
        heapq.heappush(genres_rank, (-plays_dic[g], g))
    
    genres_cnt = defaultdict(int)
    result = []
    while genres_rank:
        genre = heapq.heappop(genres_rank)[1]
        
        while dic[genre]:
            genres_cnt[genre] += 1
            result.append(heapq.heappop(dic[genre])[1])
            if genres_cnt[genre] >= 2:
                break

    return result