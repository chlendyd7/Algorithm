# n=3
# dy = [0]*(n+1)
# #print(dy)
# for i in range(n+1):
#     dy[i] = i
#     print(dy[i])

#for문은 시작부터 그 갯수만큼 돌아감 마지막 숫자는 -1 왜냐하면 0을 사용하기 때문
# 0 1 2
#1부터 18까지 사용하고 싶다면 1, n+1을 해줘야함
# 1 2 3


#뒤로가는 경우는 생각한대로 나옴 0을 안하기 때문
#3 2 1
n=int(input())
dis=[[5000]*(n+1) for _ in range(n+1)]
print(dis)