n, l = map(int, input().split())
wong_dung = [list(map(int, input().split())) for _ in range(n)]
wong_dung.sort()

current_end = 0
cnt = 0

for s, e in wong_dung:
    if current_end >= e:
        continue

    start = max(s, current_end)
    num_planks = (e - start + l - 1) // l
    current_end = s + num_planks * l
    cnt += num_planks

print(cnt)
