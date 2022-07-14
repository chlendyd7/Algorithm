from posixpath import split


num1,num2 = map(int, input().split())

print('>') if num1 > num2 else print('<') if num1 < num2 else print('==')