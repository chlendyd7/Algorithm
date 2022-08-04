N = int(input())

for i in range(N):
    ox_list = list(input())
    score = 0
    sum = 0
    for ox in ox_list:
        if ox =='O':
            score +=1
            sum +=score
        else:
            score = 0
    print(sum)        
