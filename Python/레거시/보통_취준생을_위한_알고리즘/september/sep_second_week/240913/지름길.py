'''
    다익스트라도 한번 만들어보기
'''
n, d = map(int,input().split())
high_way_lst = []
for _ in range(n):
    start, end, dist = map(int, input().split())
    if end - start > dist:
        high_way_lst.append((start, end, dist))

distance = [0] * (d+1)
for i in range(d+1):
    distance[i] = i

for high_way in high_way_lst:
    for i in range(1, d+1):
        if i == high_way[1]:
            distance[i] = min(distance[i], distance[high_way[0]] + high_way[2])
        else:
            distance[i] = min(distance[i], distance[i-1] + 1)

print(distance[d])
