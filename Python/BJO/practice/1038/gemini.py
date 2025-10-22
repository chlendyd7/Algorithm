N = int(input())
nums = []

# DFS를 이용해 감소하는 수를 생성하는 함수
# num_str: 현재까지 만들어진 감소하는 수 (문자열)
# last_digit: num_str의 마지막 자릿수 (현재 자릿수보다 작은 수만 올 수 있도록 기준 설정)
def dfs(num_str, last_digit):
    # num_str은 이미 nums에 추가되었으므로, 다음 자릿수를 붙이는 것부터 시작
    
    # 즉, 0부터 (last_digit - 1)까지 가능하다.
    for i in range(last_digit): # range(last_digit)는 0부터 last_digit-1 까지
        next_num_str = num_str + str(i)
        
        nums.append(int(next_num_str))
        
        dfs(next_num_str, i)


# 1. 0부터 9까지의 한 자리 감소하는 수 (N=0부터 N=9)를 먼저 리스트에 추가
# 이 수들이 감소하는 수의 가장 첫 번째 그룹이다.
for i in range(10):
    nums.append(i)

# 2. 2자리 이상의 감소하는 수 생성
# 1부터 9까지의 각 숫자를 시작으로 DFS 호출 (0은 첫 자리에 올 수 없음)
for i in range(1, 10):
    # i를 문자열로 시작하고, 다음 자릿수는 i보다 작아야 하므로 i를 기준값으로 전달
    dfs(str(i), i)

# 3. 모든 감소하는 수를 오름차순으로 정렬
nums.sort()

# 4. N번째 감소하는 수 출력
# N번째 수는 리스트의 인덱스 N에 해당한다. (인덱스는 0부터 시작)
# N이 리스트의 길이보다 크거나 같으면, N번째 감소하는 수는 존재하지 않는다.
if N >= len(nums):
    print(-1)
else:
    print(nums[N])
