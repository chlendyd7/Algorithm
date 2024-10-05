def solution(a,b,c):
    s = list()
    answer = 0
    for i in range(len(b)):
        s.append((b[i], c[i]))
    
    s.sort(key=lambda x: x[1])
    for i in a:
        cnt = 0
        for j in range(len(b)):
            i = i 
    
    print(s)

a =[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230]
b = [7, 3, 9]
c = [9, 10, 1]
print(solution(a,b,c))