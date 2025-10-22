n = int(input())
people = 0
vilage = []

for _ in range(n):
    pos, peo = map(int, input().split())
    vilage.append((pos, peo))
    people += peo

vilage.sort(key=lambda x: x[0])

cnt = 0
for pos, peo in vilage:
    cnt += peo
    if cnt >= people / 2:
        print(pos)
        break
