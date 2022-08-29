T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    people = [i for i in range(1, 1+n)]

    for j in range(k):
        for x in range(1, n):
            people[x] += people[x-1]
    print(people[-1])