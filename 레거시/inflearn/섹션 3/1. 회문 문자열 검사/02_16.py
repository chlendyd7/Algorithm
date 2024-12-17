n = int(input())

for i in range(n):
    word=input()
    word=word.lower()
    for j in range(len(word)//2):
        if word[j] != word[-j-1]:
            print(f'#{i+1} NO')
            break
    else:
        print(f'#{i+1} YES')