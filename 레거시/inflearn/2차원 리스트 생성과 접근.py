'''
2차원 리스트 생성과 접근
'''
a = [[0]*3 for _ in range(3)]
#print(a)

for x in a:
    print(x)

for x in a:
    for y in x:
            print(y, end=' ')
    print()
        
