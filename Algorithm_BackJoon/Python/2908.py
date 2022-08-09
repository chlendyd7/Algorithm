num1, num2 = input().split()
num1 = num1[::-1]
num2 = num2[::-1]
print(num1) if num1 > num2 else print(num2)