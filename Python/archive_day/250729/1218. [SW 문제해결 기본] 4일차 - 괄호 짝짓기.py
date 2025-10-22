N = int(input())
result = []

for k in range(N):
    tc = int(input())

    num_lst = list(map(int, input().split()))

    # number이 나온 갯수를 구하는 로직
    empty = []
    for number in num_lst:
        n = 0
        for i in range(1000):
            if num_lst[i] == number:
                n += 1
        empty.append(number)

    # index로 접근
    result_list = []
    num2 = -1
    mx_cnt = max(empty)
    for cnt in empty:
        num2 += 1
        if cnt == mx_cnt:
            result_list.append(num2)

    # print(list(map(lambda x: a[x],result_list)))

    result.append(f"# {tc} {max(list(map(lambda x: num_lst[x], result_list)))}")

for r in result:
    print(r)
