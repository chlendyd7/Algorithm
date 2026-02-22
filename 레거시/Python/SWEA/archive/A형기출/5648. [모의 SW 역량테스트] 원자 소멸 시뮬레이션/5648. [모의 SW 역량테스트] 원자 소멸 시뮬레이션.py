'''


    N <= 1000
    K 보유 에너지
    상하좌우 0,1,2,3
    1초에 1만큼 이동
'''
di, dj = (1,-1,0,0), (0,0,-1,1)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    for i in range(len(arr)):
        arr[i][0] *=2 #왜 이렇게 해주는가?
        arr[i][1] *=2 # 그 이유는 1.5초 뒤에 만나는 원자들이 있기에 *2을 처리해줌
    ans = 0

    for _ in range(4001): #왜 4001 최악의 경우 끝에서 끝 1000~1000인데 2배 했으니 4000
        for i in range(len(arr)):
            arr[i][0] += di[arr[i][2]]
            arr[i][1] += dj[arr[i][2]]

        v, ddel = set(), set()
        for i in range(len(arr)):
            cj, ci = arr[i][0], arr[i][1]
            if (cj,ci) in v:
                ddel.add((cj,ci))
            else:
                v.add((cj,ci))
            
        for i in range(len(arr)-1, -1, -1):
            if (arr[i][0], arr[i][1]) in ddel:
                ans += arr[i][3]
                arr.pop(i)
            elif max(abs(arr[i][0]), arr(arr[i][1])) >2000:
                arr.pop(i)
        
        if len(arr)<2:
            break
    print(f'#{tc} {ans}')
