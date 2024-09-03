class Node:
    def __init__(self) -> None:
        self.value = False
        self.childs = {}

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, phone_num):
        curNode = self.root
        for num in phone_num:
            if num not in curNode.childs:
                curNode.childs[num] = Node()
            curNode = curNode.childs[num]
            if curNode.value is True: #현재 노드가 문자열의 끝이라면 노드는 True로 표시한다
                return False
        curNode.value = True
        return True

for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    phone_list = [input().rstrip() for _ in range(n)]
    phone_list.sort()
    trie = Trie()
    for num in phone_list:
        tof = trie.insert(num)
        if not tof:
            break
    if tof:
        print('YES')
    else:
        print('NO')