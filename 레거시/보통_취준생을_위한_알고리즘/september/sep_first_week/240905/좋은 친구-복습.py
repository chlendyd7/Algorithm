
from collections import deque


n, k = map(int,input().split())
name_length_dic = dict()
for i in range(2, 21):
    name_length_dic[i] = deque()

cnt = 0
for i in range(n):
    length = len(input())
    
    if name_length_dic[length]:
        while name_length_dic[length] and i - name_length_dic[length][0] > k:
            name_length_dic[length].popleft()
        cnt += len(name_length_dic[length])
    
    name_length_dic[length].append(i)

print(cnt)