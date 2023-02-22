n = int(input())

for i in range(n):
    word = input()
    word=word.lower()
    for j in range(len(word)//2):
        if word[j] != word[-1-j]:
            print("#%d NO" %(i+1))
            break
    
        print('#%d YES' %(i+1)) 
# n = "word"
# print(n[-2])