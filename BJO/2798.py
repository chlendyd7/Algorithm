n, m = map(int, input().split())
ls = list(map(int, input().split()))
sum = 0
for i in range(n):
    for j in range(i+1, n):
        for z in range(j+1, n):
            card_combi = ls[i]+ls[j]+ls[z]
            if card_combi <= m:
                sum = max(sum, card_combi)
print(sum)
