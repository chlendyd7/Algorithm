n = int(input())
for i in range(n):
    s = input()
    s = s.lower()
    #l_alp = list(alp)
    # for z in range(len(alp)//2):
    #     if alp[z] == alp[-1-z]:
    #         print("#%d YES" %(i+1))
    #         break
    #     else:
    #         print("#%d NO" %(i+1))
    size = len(s)
    for j in range(size//2):
        if s[j] != s[-1-j]:
                print("#%d NO" %(i+1))
                break
    else:
        print("#%d YES" %(i+1))        #if문 통과하지 않고 정상적으로 올 시 통과

    


# n = int(input())
# for i in range(n):
#     s = input()
#     s=s.upper()
#     if s==s[::-1]:
#         print("#%d YES" %(i+1))
#     else:
#         print("#%d NO" %(i+1))