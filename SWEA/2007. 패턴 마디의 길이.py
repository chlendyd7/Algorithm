def find_pattern_length(s):
    for i in range(1, 11):  # 마디 길이 i
        matched = True
        for j in range(i, 30):
            if s[j] != s[j % i]:
                matched = False
                break
        if matched:
            return i
    return 30

def find_pattern_length(s):
    for i in range(1, 11):  # 마디 길이는 최대 10까지
        pattern = s[:i]
        repeated = pattern * (30 // i)
        if s.startswith(repeated[:30]):
            return i
    return 30  # fallback (문제 조건상 안 나올 것)

T = int(input())
for t in range(1, T + 1):
    s = input()
    result = find_pattern_length(s)
    print(f"#{t} {result}")