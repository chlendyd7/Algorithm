T = int(input())
 
for testcase in range(1, T + 1):
    N, M = map(int, input().split())
 
    arr = list(input().split())
 
    i_j_pairs = [tuple(input().split()) for _ in range(M)]
 
    for i, j in i_j_pairs:
        i, j = int(i), int(j)
        for num in range(1, j + 1):
            left = i - 1 - num
            right = i - 1 + num
 
            if 0 <= left < N and 0 <= right < N:
                if arr[left] == arr[right]:
                    if arr[left] == '0':
                        arr[left] = arr[right] = '1'
                    elif arr[left] == '1':
                        arr[left] = arr[right] = '0'
 
    print(f"#{testcase} {' '.join(arr)}")
