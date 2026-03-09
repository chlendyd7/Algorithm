import sys
import os
file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

# 파일이 존재하는지 확인 후 stdin을 교체합니다.
if os.path.exists(file_path):
    sys.stdin = open(file_path, 'r')
else:
    print("경고: input.txt 파일을 찾을 수 없습니다.")

S = input()
K, M = map(int, input().split())
L = len(S)
current_hash = int(S[:K], 2)
counts = {current_hash: 1}
mask = (1 << K) - 1 # 이러면 1000 - 1 => 이진수로 변환되서 처리되나 111

for i in range(K, L):
    new_bit = int(S[i])
    # hashmap 하나 미는건 이해되는데 그 뒤 잘 모르겟음
    current_hash = ((current_hash << 1) | new_bit) & mask
    counts[current_hash] = counts.get(current_hash, 0) + 1

    if counts[current_hash] >= M:
        print(1)
        break

print(0)

    

    