N,K = map(int,input().split())
bag = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if j >= bag[i-1][0]:
            dp[i][j] = max(bag[i-1][1]+dp[i-1][j-bag[i-1][0]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][K])

#https://claude-u.tistory.com/208

'''
설명
누적합 풀이로
소문자 a~z까지 총 26개 * name의 길이 로 2차원 배열을 생성
a~z를 아스키코드로 변환 한 뒤에 -97을 하면 0~25까지 된다

그리고 arr[i][j] += arr[i-1][j] + 현재i번째 위치에 알파벳 아스키코드-97
을 해서 0번째 부터 끝까지 누적으로 몇개 나왔는지 전부 2차원 배열안에 넣는다.
그래서 i~j번째 까지 알파벳이 몇개 나왔는지 확인하려면
arr[i][askii] - ar[j-1][askii]
i~j번째 까지 나온 알파벳askii의 개수를 알 수 있다.

예외처리
0~i번재 까지라면 arr[i][askii] - 0 을 해줘야한다.
'''