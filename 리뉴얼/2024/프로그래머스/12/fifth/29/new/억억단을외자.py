import math
MAX = 5_000_001
def solution(e, starts):
    cnt = [1]*(e+1)
    for num in range(1,e+1):
        for increment in range(num*2,e+1,num):
            cnt[increment]+=1
# -------------------            
    
    # dp[n] : [n,e] 구간의 최댓값의 idx(=가장 큰 약수의 개수의 idx)
    dp = [0] *(e+1)
    dp[e] = e
    maxVal = cnt[e]
    for i in reversed(range(1,e)):
        # cnt[i]의 값이 [i+1,e]의 최댓값보다 큰 경우(= 더 많이 등장한 경우)
        if cnt[i] >= cnt[dp[i+1]]:
            dp[i] = i
        else:
            dp[i] = dp[i+1]
    
    answer = []
    for start in starts:
        answer.append(dp[start])
    return answer
