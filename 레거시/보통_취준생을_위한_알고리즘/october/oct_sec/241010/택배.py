n, limit = map(int, input().split())
m = int(input())
boxs = [list(map(int, input().split())) for _ in range(m)]
boxs.sort(key=lambda x:x[1])
trucks = [limit] * n
result = 0
for box in boxs:
    min_box = limit
    for i in range(box[0], box[1]):
        min_box = min(min_box, trucks[i])
    min_box = min(min_box, box[2])

    for j in range(box[0], box[1]):
        trucks[j] -= min_box
    result += min_box

print(result)