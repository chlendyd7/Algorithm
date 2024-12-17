'''
    소스 하나를 정해두고 나머지 어울리는 값을 구하는 이분탐색을 만들면 된다
'''

n = int(input())
liquids = list(map(int,input().split()))

left = 0
right = n-1

ans = float("INF")
ans_left = 0
ans_right = 0

for i in range(n-1):
    current = liquids[i]
    start = i + 1
    end = n - 1

    while start < end:
        mid = (left + right) // 2
        tmp = current + liquids[mid]

        if abs(tmp) < ans:
            ans_left = i
            ans_right = mid

            if tmp == 0:
                break
        if tmp < 0:
            start = mid + 1
        else:
            end = mid -1
print(liquids[ans_left], liquids[ans_right])

