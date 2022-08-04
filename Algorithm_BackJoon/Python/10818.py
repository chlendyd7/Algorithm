from posixpath import split


num1,num2 = map(int, input().split())

print('<') if num1 < num2 else print('==')

cnt = int(input())
numbers = list(map(int, input().split()))

max = numbers[0]
min = numbers[0]