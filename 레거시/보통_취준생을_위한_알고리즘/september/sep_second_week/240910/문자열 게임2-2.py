import sys
from collections import defaultdict

t=int(sys.stdin.readline())

for _ in range(t): #테스트 케이스 수만큼 반복.
    string=sys.stdin.readline().rstrip()
    n=int(sys.stdin.readline())
    
    dic=defaultdict(list) #key값이 없으면 빈 리스트라도 넣게하기위해! (*defulatdict*)

    for i in range(len(string)):
        if string.count(string[i])>=n: #개수가 n개 이상인 문자들에 대해서만,
            dic[string[i]].append(i) #문자별로 좌표를 저장.(ex [a]:[0, 4, 9])
 

    if not dic: #n개 이상인 문자 없으면 아예 불가능.
        print(-1)
    else:
        small=10000 #최소를 일단 최대값으로 세팅. (여기서 더 작아질 거임)
        big=1 #최대를 일단 최소값으로 세팅. (여기서 더 커질 거임)
        
        for alpha in dic: #dic에 있는 특정 문자 alpha에 대해,
            for i in range(len(dic[alpha])-n+1): #특정문자의 개수-필요한 개수+1 만큼 가능(생각해보면 아는 사실)
                length=dic[alpha][i+n-1]-dic[alpha][i]+1 #특정 문자의 좌표들간의 간격 + 1이 문자열 길이가 된다!

                #최소, 최대를 계속 최신화 시켜준다.
                small=min(small,length)
                big=max(big,length)

        print(small,big)
