def digit_sum(x):
    sum=0
    for i in str(x):
        sum += int(i)
    return sum
        






if __name__=="__main__":
    n = int(input())
    max = 0
    ls = list(map(int,input().split()))
    for i in ls:
        tot = digit_sum(ls)
        if tot > max:
            max = tot
            res = i
    print(i)
