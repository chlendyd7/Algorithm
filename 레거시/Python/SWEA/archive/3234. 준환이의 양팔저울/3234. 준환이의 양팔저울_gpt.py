times = int(input())

def put(idx, left, right, p):
    global n, result, sum_weights

    if idx == n:  # 모든 추를 다 올린 경우
        result += 1
        return

    # 왼쪽 무게가 전체 절반보다 크면 오른쪽에 뭘 올려도 항상 안전
    if left > sum_weights // 2:
        cnt = 1
        for _ in range(n - idx):
            cnt *= 2  # 2^(n-idx)
        result += cnt
        return

    # 왼쪽에 올리기
    put(idx + 1, left + p[idx], right, p)

    # 오른쪽에 올리기 (조건 만족 시만)
    if right + p[idx] <= left:
        put(idx + 1, left, right + p[idx], p)


def perm(length, now, remaining):
    global n
    if length == n:
        put(0, 0, 0, now)
        return
    for i in range(len(remaining)):
        perm(length + 1, now + [remaining[i]], remaining[:i] + remaining[i + 1:])


for t in range(times):
    n = int(input())
    weights = list(map(int, input().split()))
    sum_weights = sum(weights)
    result = 0
    perm(0, [], weights)
    print(f"#{t+1} {result}")
