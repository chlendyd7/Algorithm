def solution():
    N = int(input())
    result = ''
    for _ in range(N):
        alp, n = input().split()
        result += alp * int(n)
    for i in range(0, len(result), 10):
        print(''.join(result[i:i+10]))


T = int(input())
for t in range(1, T+1):
    print(f'#{t}')
    solution()