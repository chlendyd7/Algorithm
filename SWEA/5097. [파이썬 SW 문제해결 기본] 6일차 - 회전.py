T = int(input())
for i in range(1, T+1):
    n, m = map(int, input().split())
    nums = list(map(int,input().split()))
    print(f'#{i} {nums[m%n]}')
