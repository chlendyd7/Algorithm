'''
추를 올릴 때 왼쪽 > 오른쪽
무게추를 올리는 방법의 갯수는?

백트래킹 + 가지치기 문제
'''

def solution():
    N = int(input())
    chus = list(map(int, input().split()))
    used = [0] * N
    cnt = 0

    def dfs(left, right, total):
        nonlocal cnt
        if total == N:
            cnt += 1
            return

        for i in range(N): # 중복을 어떻게 해결하지?
            if not used[i]:
                used[i] = True
                dfs(left + chus[i], right, total + 1)

                if not right + chus[i] > left:
                    dfs(left, right + chus[i], total + 1)
                used[i] = False

    dfs(0, 0, 0)
    return cnt


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
