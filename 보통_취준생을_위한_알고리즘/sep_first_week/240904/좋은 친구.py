from collections import deque

# 입력 받기
n, k = map(int, input().split())  # n: 학생 수, k: 등수 차이
name_lengths = [len(input().strip()) for _ in range(n)]

# 각 이름 길이에 해당하는 인덱스를 저장할 큐를 초기화합니다.
queue_dict = {}
for i in range(2, 21):  # 이름 길이는 2부터 20까지이므로
    queue_dict[i] = deque()

good_friend_pairs = 0

# 각 학생의 이름 길이에 대해 처리
for i in range(n):
    length = name_lengths[i]
    
    # 현재 학생의 이름 길이에 해당하는 큐에 대해
    if queue_dict[length]:
        # 큐의 맨 앞에 있는 값이 현재 등수(i)에서 K를 초과하면 큐에서 제거
        while queue_dict[length] and i - queue_dict[length][0] > k:
            queue_dict[length].popleft()
    
        # 좋은 친구 쌍의 수를 계산 (큐에 남아있는 요소의 수가 현재 좋은 친구의 수)
        good_friend_pairs += len(queue_dict[length])
    
    # 현재 학생의 등수를 큐에 추가
    queue_dict[length].append(i)

# 결과 출력
print(good_friend_pairs)
