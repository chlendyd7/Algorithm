n,k = map(int,(input().split()))
number = list(input())

cnt = k

answer = []
for num in number:
    while answer and cnt > 0 and answer[-1] < num:
        answer.pop()
        cnt -= 1
    answer.append(num)

if cnt>0:
    answer = answer[:-cnt]

print(''.join(answer))
