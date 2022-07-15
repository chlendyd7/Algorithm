#시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

from os import listdir
from re import L


score = list(map(int, input("시험 점수를 입력 하세요").split()))
score = score[0]
if (score > 89):
    print("A")
elif score > 79:
    print("B")
elif score > 69:
    print("C")
elif score > 59:
    print("D")
elif score > 0:
    print("F")
else:
    print("잘 못 입력하셨습니다")

list_a = [1,2,3,4,5,6,7,8,9]
num1 = 0
num2 = 0
for a in list_a:
    if a%2 ==0:
        num1+=a
    else:
        num2+=a
print(f"list_a 홀수 합: {num1}, 짝수 합: {num2}")

list_b = [51,45,78,95,1,500,460,1054]


print(list_b)

def select_sort(l):
  for i in range(len(l)-1):
    for j in range(len(l)-1-i):
      if l[j] > l[j+1]:
        l[j], l[j+1] = l[j+1], l[j]

def select_sort_down(l):
    for i in range(len(l)-1):
        for j in range(len(l)-1-i):
            if l[j]< l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

select_sort(list_b)
print(list_b)
select_sort_down(list_b)
print(list_b)


list_c = [[1,2,3,4,5,7],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(len(list_c[0]))
list_d = []
for i in range(len(list_c)):
        result = (list_c[i][0])+(list_c[i][len(list_c[i])-1])  
        list_d.append(result)
print(list_d)
    