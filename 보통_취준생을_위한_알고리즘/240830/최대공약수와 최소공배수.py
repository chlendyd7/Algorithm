n,m = map(int,input().split())

def LCM(num1, num2):
    return (num1 * num2) // GCD(num1, num2)

def GCD(num1, num2):
    if num2 % num1:
        return GCD(num2 % num1, num1)
    else:
        return num1

print(GCD(n,m))
print(LCM(n,m))
