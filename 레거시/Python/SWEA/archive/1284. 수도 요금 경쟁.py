'''
- 더 적게 수도 요금을 부담해도 되는 회사
A사 1L 당 p원
B사 기본 요금Q 월간 사용량 R이하의 경우 기본 요금
R리터보다 많은 양을 사용한 경우 초과한량에 대해 1리터당 S원 의요금

종민이네 사용량 W
'''
def solution(P, Q, R, S, W):
    a_price = P * W
    if W <= R:
        b_price = Q
    else:
        b_price = Q + (W - R) * S
    
    return min(a_price, b_price)
T = int(input())
for t in range(1,T+1):
    P, Q, R, S, W = map(int, input().split())
    print(f'#{t} {solution(P,Q,R,S,W)}')
