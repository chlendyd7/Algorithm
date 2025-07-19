'''
    사재기
    1. 연속된 N일 동안의 물건을 알고있음
    2. 하루에 최대 1만큼 구매
    3. 판매는 얼마든지 가능
    greedy?
    최대 이익
    start, end를 체크해서 
    
    생각한 방법: 
'''

T = int(input())
for t in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))
    
    max_price = 0
    profit = 0

    for price in reversed(prices):
        if price > max_price:
            max_price = price
        else:
            profit += (max_price - price)

    print(f'#{t} {profit}')
