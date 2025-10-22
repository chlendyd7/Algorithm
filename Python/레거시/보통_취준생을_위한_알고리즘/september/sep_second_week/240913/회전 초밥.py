from collections import defaultdict






n,d,k,c = map(int,input().split())
chobob_lst = [int(input()) for _ in range(n)]
chobob_lst += chobob_lst[:n-1]
answer = 0

for i in range(n):
    num = len(set(chobob_lst[i:i+k] + [c]))
    answer = max(answer, num)
print(answer)