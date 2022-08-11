# input = ["aba","abab","abcabc","a"]
N=int(input())
answer = 0
for i in range(N):
    option = [">"]
    word = input()
    for j in word:
        if option[-1] != j:
            option.append(j)
    if len(option)==len(set(option)):
        answer +=1
print(answer)
