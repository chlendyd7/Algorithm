# a, b ,c = map(int,input().split())
# i = 0
# cnt=0
# if c < b :
#     print(-1)

# else:
#     while (c*i)<=(a+(b*i)):
#         cnt +=1
#         i +=1

# print(cnt)
## Ctrl + K + C 전체 주석

a,b,c = map(int, input().split())
if c<=b:
    print(-1)
else:
    print(int(a/(c-b)+1))