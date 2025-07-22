'''
    1부터 시작
    학생에게 1~N개 자연수를 나눠줌
    성별과 받은 수에 따라 다름
    남학생: 스위치 번호가 받은 수의 배수이면 상태를 바꾼다
    여학생: 같은 번호 중심
        -   좌우가 대칭, 
        -   가장 많은 스위치를 포함하는 구간,
        -   모두 바꾸기
        -   갯수는 항상 홀수
    
'''
# 남은 1 여자는 2
def convert_switch(s):
    if s == 1:
        return 0
    else:
        return 1

N = int(input())
switchs = list(map(int, input().split()))
M = int(input())

for _ in range(M):
    sex, num = map(int, input().split())
    idx = num - 1
    if sex == 1:
        for i in range(idx, N, num):
            switchs[i] = convert_switch(switchs[i])

    else:
        i = 1
        print(switchs)
        while True:
            if (idx+i) >= N-1 or (idx - i) <= 0:
                break
            if switchs[idx + i] != switchs[idx - i]:
                break
        
        i = i - 1
        for j in range(idx-i, idx+i+1):
            switchs[j] = convert_switch(switchs[j])

# print(switchs)
print(' '.join(map(str, switchs)))

