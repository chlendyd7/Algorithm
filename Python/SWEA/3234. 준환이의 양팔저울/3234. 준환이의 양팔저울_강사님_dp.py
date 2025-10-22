def solution():
    N = int(input())
    nums = list(map(int, input().split()))
    cnt = 0

    dp = [{} for _ in range(2**9)] #2의9승-1개를 확보 다 채워진 경우(비트마스크가 그래서 나옴)
    visited = 0
    def dfs(count, diff):
        nonlocal visited

        if dp[visited].get(diff):
            return dp[visited][diff]

        if count == N: #들어왔다는건 dp를 활용 할 수 없었다
            dp[visited][diff] = 1
            return dp[visited][diff]

        case_count = 0
        for i in range(N):
            if visited & (1 << i): # 비트를 i번 밀어주면 i에 도착하게됨
                continue
            
            visited |= (1 << i) #or로 밀어주면서 i를 채워줌
            case_count += dfs(count+1, diff+nums[i])
            if diff-nums[i] >= 0:
                case_count += dfs(count+1, diff-nums[i])
            visited ^= (1 << i) #xor로 다시 0으로 만들어줌

        dp[visited][diff] = case_count        
        return dp[visited][diff]

    answer = dfs(0, 0)
    


    return cnt

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
