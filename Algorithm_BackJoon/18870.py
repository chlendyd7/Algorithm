import sys
input = sys.stdin.readline
n = int(input())
ls = list(map(int,input().split()))
ls2 =sorted(set(ls))
dic = {value:index for index, value in enumerate(ls2)}

for i in ls:
    print(dic[i], end=' ')

### enumerate

# • **인자로 넘어온 목록을 기준으로 인덱스 번호와 배열의 원소를 튜플 형태로 반환**

# • start를 통해 시작 index 변경가능