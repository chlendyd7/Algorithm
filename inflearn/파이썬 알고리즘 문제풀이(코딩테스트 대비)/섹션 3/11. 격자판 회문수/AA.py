board=[list(map(int, input().split())) for _ in range(7)]
cnt=0
for i in range(3):
    for j in range(7):
        tmp=board[j][i:i+5]#슬라이싱 기능을 이용한다 
        if tmp==tmp[::-1]: #회문을 거꾸로
            cnt+=1
        for k in range(2):#5개를 검사하니 앞뒤 두개를 검사
            if board[i+k][j]!=board[i+5-k-1][j]:
                break
        else:
            cnt+=1
        
print(cnt)
