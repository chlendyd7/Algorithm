def GCD(a, b):
    if b % a:
        return GCD(b % a, a)
    else:
        return a

n,m = map(int,input().split(':'))
a = GCD(n,m)
print(f'{n//a}:{m//a}')
