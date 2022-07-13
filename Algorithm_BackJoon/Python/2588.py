input1 = int(input())
input2 = int(input())

result1 = int(input1*(input2%10))
result10 = int(input1*(input2%100 - input2%10)/10)
result100 = int(input1*(input2 - input2%100)/100)

print(result1)
print(result10)
print(result100)
print(input1*input2)