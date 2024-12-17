n,c = map(int, input().split())
m = int(input())
arr = [list(map(int, input().split())) for _ in range(m)]
arr.sort(key=lambda x:(x[1]))

trucks = [c] * (n+1)
cnt = 0
for box in arr:
    min_box = c
    for i in range(box[0], box[1]):
        min_box = min(min_box, trucks[i])
    min_box = min(min_box, box[2])
    for i in range(box[0], box[1]):
        trucks[i] -= min_box
    cnt += min_box

print(cnt)
