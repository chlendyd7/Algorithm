# https://www.codetree.ai/ko/frequent-problems/hsat/problems/car-test/description
def solve():
    n, q = map(int, input().split())
    cars = list(map(int, input().split()))
    cars.sort()
    
    pos = {val: idx for idx, val in enumerate(cars)}
    
    for _ in range(q):
        m = int(input())
        
        if m in pos:
            idx = pos[m]
            ans = idx * (n-1-idx)
            print(ans)
        else:
            print(0)