def sosu(n):
    if n ==1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
list_range = list(range(2,246912))
answer_list =[]

for i in list_range:
    if sosu(i):
        answer_list.append(i)

while True:
    cnt =0
    n = int(input())

    if n == 0:
        break

    for i in answer_list:
        if n < i < n*2+1:
            cnt +=1
    print(cnt)
