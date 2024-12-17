import heapq

num_shortcuts, highway_length = map(int, input().split())
inf = float('inf')

# 각 지점을 저장할 그래프, 총 highway_length+1 만큼 리스트를 생성
graph = [[] for _ in range(highway_length + 1)]
# 거리 리스트 초기화, 초기값을 무한대로 설정
distances = [inf] * (highway_length + 1)

# 기본적으로 1씩 이동하는 도로 설정
for i in range(highway_length):
    graph[i].append((i + 1, 1))

# 지름길 정보 입력받아 그래프에 추가
for _ in range(num_shortcuts):
    start, end, shortcut_length = map(int, input().split())
    if end <= highway_length:
        graph[start].append((end, shortcut_length))

# 우선순위 큐를 사용해 다익스트라 알고리즘 적용
priority_queue = []
heapq.heappush(priority_queue, (0, 0))  # (누적 거리, 현재 위치)
distances[0] = 0

while priority_queue:
    current_distance, current_location = heapq.heappop(priority_queue)

    # 현재 위치에서 이동할 수 있는 모든 경로 확인
    for next_location, move_distance in graph[current_location]:
        total_distance = distances[current_location] + move_distance
        if distances[next_location] > total_distance:
            distances[next_location] = total_distance
            heapq.heappush(priority_queue, (total_distance, next_location))

# 도착 지점까지의 최소 거리 출력
print(distances[highway_length])
