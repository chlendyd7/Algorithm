# import sys
# input = sys.stdin.readline

# string = input()
# q = int(input())

# for i in range(q):
#     temp = input().split()
#     sum=0
#     for j in range(int(temp[1]), int(temp[2])+1):
#         if string[j] == temp[0]:
#             sum += 1
#     print(sum)

import sys

input = sys.stdin.readline

name = input().strip()
n = int(input())
arr = [[0 for i in range(26)] for i in range(len(name))]
arr[0][ord(name[0]) - 97] = 1
for i in range(1, len(name)):
    arr[i][ord(name[i]) - 97] = 1
    for j in range(26):
        arr[i][j] += arr[i - 1][j]
print(arr)
for i in range(n):
    a = input().split()
    if int(a[1]) > 0:
        res = arr[int(a[2])][ord(a[0]) - 97] - arr[int(a[1]) - 1][ord(a[0]) - 97]
    else:
        res = arr[int(a[2])][ord(a[0]) - 97]
    print(res)


'''
설명
누적합 풀이로
소문자 a~z까지 총 26개 * name의 길이 로 2차원 배열을 생성
a~z를 아스키코드로 변환 한 뒤에 -97을 하면 0~25까지 된다

그리고 arr[i][j] += arr[i-1][j] + 현재i번째 위치에 알파벳 아스키코드-97
을 해서 0번째 부터 끝까지 누적으로 몇개 나왔는지 전부 2차원 배열안에 넣는다.
그래서 i~j번째 까지 알파벳이 몇개 나왔는지 확인하려면
arr[i][askii] - ar[j-1][askii]
i~j번째 까지 나온 알파벳askii의 개수를 알 수 있다.

예외처리
0~i번재 까지라면 arr[i][askii] - 0 을 해줘야한다.
'''