facto = [0, 1]
for i in range(2, 10):
    facto.append(facto[i - 1] * i)


def put(idx, left, right, p):
    global N, result, sum_w

    if idx == N:            # left, right 에 다 나눠담았을 경우
        result += 1
        return
    if left > sum_w // 2:   # left 가 모든 추 무게의 합 절반을 넘었으면 나머지는 안 봐도 됨 => 남은 숫자들을 left/right 에 넣는 경우의 수 더함
        n = N - idx
        result += (2 ** n)
        return

    # left 에 추를 올릴 경우
    put(idx + 1, left + p[idx], right, p)
    # right 에 추를 올릴 경우
    if right + p[idx] <= left:
        put(idx + 1, left, right + p[idx], p)


def perm(length, now, remaining):
    # 순열이 완성될 때마다 put 함수 호출
    if length == N:
        put(0, 0, 0, now)
        return

    for i in range(len(remaining)):
        perm(length + 1, now + [remaining[i]], remaining[:i] + remaining[i + 1:])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    weights = list(map(int, input().split()))
    sum_w = sum(weights)
    result = 0
    perm(0, [], weights)

    print('#{} {}'.format(tc, result))