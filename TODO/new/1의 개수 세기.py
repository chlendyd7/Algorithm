def count_ones(x):
    if x < 0:
        return 0

    count = 0
    i = 0
    while (1 << i) <= x:
        # 각 자리수마다 1의 개수를 계산
        full_cycles = (x + 1) // (1 << (i + 1))
        remainder = (x + 1) % (1 << (i + 1))
        count += full_cycles * (1 << i)  # 완전한 사이클에서 1이 등장하는 횟수
        count += max(0, remainder - (1 << i))  # 남은 부분에서 1이 추가로 등장하는 횟수
        i += 1
    return count

# 입력 처리
A, B = map(int, input().split())

# A에서 B까지의 1의 개수는 f(B) - f(A-1)
result = count_ones(B) - count_ones(A - 1)

# 결과 출력
print(result)
