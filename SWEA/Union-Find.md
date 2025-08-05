# 유니온-파인드(Union-Find)
[참조](https://chiefcoder.tistory.com/55)
유니온-파인드 자료구조는 서로 중복되는 원소가 전혀 없는(교집합이 공집합인) 부분 집합들을 말함

핵심 연산
1. Find: 특정 원소가 속한 집합의 '대표 원소(Representative)'를 찾는 연산
2. Union: 두 개의 서로 다른 집합을 하나의 집합으로 합치는 연산

## 구현 코드
```Python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # 부모 노드 초기화
        self.rank = [0] * n           # 트리의 높이(랭크)

    def find(self, x):
        # 경로 압축
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA == rootB:
            return False  # 이미 같은 집합

        # 랭크 기반으로 합치기
        if self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
        elif self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
        else:
            self.parent[rootB] = rootA
            self.rank[rootA] += 1
        return True

    def connected(self, a, b):
        return self.find(a) == self.find(b)
```

```Python
uf = UnionFind(5)  # 0 ~ 4 까지 5개의 원소

uf.union(0, 1)
uf.union(1, 2)

print(uf.connected(0, 2))  # True
print(uf.connected(0, 3))  # False

uf.union(3, 4)
print(uf.find(4))  # 3 (4의 루트는 3)
```

### 구조
**트리 구조**를 사용해서 구현, 각 원소는 자신의 부모를 가르키고 부모가 없는 원소가 해당 집합의 대표 원소가 됨

parent 배열: 각 원소의 부모를 저장하는 배열 `parent[i]`는 원소 `i`의 부모를 나타냄
`parent[i] = i` 인 경우 i는 자신이 속한 집합의 대표 원소

#### 1. Find(x)연산
Find(x) 함수는 원소`x`가 속한 집합의 대표 원소를 재귀적으로 찾아 올라감
- x가 자기 자신을 부모로 가지고 있다면 (parent[x]==x), x는 대표 원소이므로 `x`를 반환
- 그렇지 않다면 `x`의 부모를 따라 계속 올라감(`Find(parent[x])`)

최적화: 경로 압축(Path Compression)
Find 연산을 수행하며 모든 노드들이 최종 대표 원소를 직접 가르키도록 부모를 갱신함
 ```
 R (대표)
  |
  A
  |
  B
  |
  C
Find(C)를 하면 C -> B -> A -> R 순으로 올라가 R을 찾습니다.

경로 압축 후 (Find(C) 수행 완료):

  R (대표)
  | \ \
  A B C  (모든 노드가 직접 R을 가리키도록 변경)
```
