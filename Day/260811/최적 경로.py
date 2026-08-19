# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=5&problemLevel=6&problemLevel=7&problemLevel=8&contestProbId=AV15OZ4qAPICFAYD&categoryId=AV15OZ4qAPICFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=8&pageSize=30&pageIndex=1

'''
    N명의 고객을 방문하고 자신의 집에 돌아감
    위치는 맨해튼 값
    가장 짧은 것을 찾으려함
    2명 ~ 10명 사이 고객 좌표
    모두 방문
    이동거리가 가장 짧은 경로
'''

from itertools import combinations, permutations
def solution():
    n = int(input())
    data = list(map(int, input().split()))
    x, y = data[0], data[1]
    ex, ey = data[2], data[3]
    houses = []
    for i in range(4, n*2+3, 2):
        houses.append((data[i], data[i+1]))

    mn = 1e9
    for lst in permutations(houses):
        temp = 0
        cx, cy = x, y
        for xx, yy in lst:
            temp += (abs(cx - xx) + abs(cy - yy))
            cx = xx
            cy = yy


        temp += (abs(cx - ex) + abs(cy - ey))
        mn = min(mn, temp)
    
    return mn


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
