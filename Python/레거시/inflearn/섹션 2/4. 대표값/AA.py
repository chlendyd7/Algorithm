import sys
#sys.stdin = open("input.txt","r")
N = int(input())
a = list(map(int,input().split()))
#파이썬 round_half_even 사용 짝수 쪽으로 감
ave = int(sum(a)/N+0.5)#소수 첫째자리에서 반올림함
min = float('inf')
for idx, x in enumerate(a):
    tmp=abs(x-ave)#절대값으로 평균과의 거리를 구해줌
    if tmp < min:
        min = tmp
        score = x
        res = idx+1 # 0번 index를 가진 실제 번호는 1이기 때문
    elif tmp == min: # 같은 경우
        if x > score: # 점수 높은 경우 이미 그 전 index값이 들어있기 때문에 같은 값이 들어오게 되면 바꾸지 않는다.
            score=x
            res=idx+1
print(ave, res)