#수정 필요
cnt = int(input())
q = dict()

for i in range(cnt):
    word = input()
    q[word] = 1

for i in range(cnt-1):
    word = input()
    q[word] = 0

for key, val in q.items():
    if q[val] == 1:
        print(q[key])
        break

