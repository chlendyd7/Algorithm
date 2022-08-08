n = int(input())

for i in range(n):
    a = list(map(int, input().split()))
    result = 0
    cnt =0
    avg = sum(a[1:])/a[0]
    for score in a[1:]:
        if score > avg:
            cnt +=1
    rate = cnt/a[0] *100
    print(f'{rate:.3f}%')