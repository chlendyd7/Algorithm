def solution(num):
    triangle = []

    for i in range(num):
        result = [1] * (i+1)
        for j in range(1, i):
            result[j] = triangle[i-1][j-1] + triangle[i-1][j]
    
        triangle.append(result)

    return triangle

T = int(input())
for t in range(1, T+1):
    print(f'#{t}')
    n = int(input())
    result = solution(n)
    for row in result:
        print(' '.join(map(str, row)))
