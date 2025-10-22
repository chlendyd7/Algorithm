'''
첫 번째 코드는 right < n일 때만 루프가 실행되므로, right가 배열 끝에 도달한 후에도 left를 움직이면서 최소 길이를 체크하는 과정이 빠집니다. 이로 인해 right가 끝에 도달했을 때 최종 결과가 반영되지 못할 수 있습니다.

예를 들어, 배열의 마지막 구간에서 합이 s 이상이 되는 경우, 첫 번째 코드에서는 right가 n에 도달하면서 더 이상 그 구간을 체크하지 않고 종료됩니다. 반면, 두 번째 코드에서는 right == n 조건에서 종료되기 전에 left를 계속 이동시켜서 최소 길이를 갱신할 수 있습니다.
'''
n,s = map(int, input().split())
nums = list(map(int,input().split()))
left, right = 0, 0

cnt = 0
answer = 1e9
while right < n:
    if cnt >= s:
        answer = min(answer, right - left)
        cnt -= nums[left]
        left += 1
    else:
        cnt += nums[right]
        right += 1

if answer == 1e9:
    print(0)
else:
    print(answer)