from collections import deque


n, m = map(int,input().split())
Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))] # enumrate?
# enumerate
# 반복문 사용 시 몇 번째 반복문인지 확인이 필요할 수 있습니다. 이때 사용합니다.
# 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환합니다.
# enumrate의 앞 pos 값은 index를 나타냄
Q = deque(Q)
cnt = 0
while True:
    cur = Q.popleft()
    if any(cur[1]<x[1] for x in Q): # any 단 한개라도 참이면 참
        Q.append(cur)
    else:
        cnt +=1
        if cur[0]==m:
            print(cnt)
            break