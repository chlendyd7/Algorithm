'''
1. 역순으로 접근
2. 가장 큰 값이면 idx를 기록
3. 같은 값이면 idx를 기록하고 있는 곳에서 합함

4. 아니였음 그냥 해당 빌딩이 얼마나 떨어지는지 구현하면 됨
5. 더 최적화가 있을까?
'''

def solution():
    n = int(input())
    buildings = list(map(int, input().split()))
    mx = -1
    cnt = 0
    for i in range(n):
        tmp = 0
        for j in range(i, n):
            if buildings[i] > buildings[j]:
                tmp +=1
        cnt = max(cnt, tmp)
    return cnt


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')