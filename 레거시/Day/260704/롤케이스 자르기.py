'''
    토핑들의 종류에
    공평하게 자르는 방법의 수
    처음 set을 해서 갯수를 파악?
    key 값을 가지고 있고 해당 값이 0이 되면 del
    길이를 항상 체크하기
    차이를 계속 all_check 안에 + 하기
    
    0이 어떻게 나와야하지?
    아 all_check의 0만 return 하면 되겠구나
    왜냐하면 같은 수 이니까
    
    for문 한번만 돌고 계속해서 
'''
from collections import defaultdict
def solution(topping):
    l_check = dict()
    r_check = dict()
    all_check = defaultdict(int)
    for t in topping:
        r_check[t] = r_check.get(t,0) + 1

    
    for t in topping:
        l_check[t] = l_check.get(t, 0) + 1
        r_check[t] = r_check.get(t,0) - 1
        
        if r_check[t] == 0:
            del r_check[t]
    
        all_check[len(l_check.keys()) - len(r_check.keys())] += 1
    
    return all_check[0]



from collections import Counter

def solution(topping):
    # 오른쪽 조각의 토핑 빈도수를 먼저 계산 (Counter 활용)
    r_check = Counter(topping)
    l_check = set()  # 왼쪽 조각은 종류만 중요하므로 set 사용
    
    answer = 0
    
    for t in topping:
        l_check.add(t)
        r_check[t] -= 1
        
        # 오른쪽에서 토핑이 다 빠지면 딕셔너리에서 제거
        if r_check[t] == 0:
            del r_check[t]
        
        # 양쪽 조각의 토핑 종류 개수(len) 비교
        if len(l_check) == len(r_check):
            answer += 1
            
    return answer


'''
리스트나 문자열처럼 반복 가능한(iterable) 객체를 입력하면, 각 요소가 몇 번 등장하는지를 딕셔너리 형태로 아주 쉽게 계산해 줍니다.
'''

from collections import Counter

# 예시: 토핑 배열
topping = [1, 2, 1, 3, 1, 4, 1, 2]

# Counter 객체 생성
result = Counter(topping)

print(result)
# 출력 결과: Counter({1: 4, 2: 2, 3: 1, 4: 1})
