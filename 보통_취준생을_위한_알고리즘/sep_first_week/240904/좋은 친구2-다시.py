from collections import deque


n,k = map(int,input().split())
name_len = [len(input()) for _ in range(n)]

queue_dict = {}
for i in range(2, 21):
    queue_dict[i] = deque()

good_friends_pairs = 0

for i in range(n):
    length = name_len[i]
    
    # if queue_dict[length]:
    while  queue_dict[length] and i - queue_dict[length][0] > k:
        queue_dict[length].popleft()

    good_friends_pairs += len(queue_dict[length])
    queue_dict[length].append(i)
print(good_friends_pairs)