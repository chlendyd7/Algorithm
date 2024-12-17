n = int(input())
body = []
for i in range(n):
    a, b = map(int,input().split())
    body.append((a,b))
body.sort(reverse=True)#몸무게로 정렬하고
print(body)
largest = 0
cnt = 0
for x,y in body:
    if y>largest: #키가 largest보다 작으면 바뀐다
        largest = y
        cnt += 1

print(cnt)


