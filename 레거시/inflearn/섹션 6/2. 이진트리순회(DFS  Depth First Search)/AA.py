#전위 순회 연습
def DFS(v):
    if v>7:
        return
    else: # 양 갈래로 뻣는 법
        # 함수 본연의 일, 호출하기 전 할 시 전위 순회
        print(v, end='')
        DFS(v*2)# 왼쪽 노드 
        # 가운데는 중위
        DFS(v*2+1)# 오른쪽 노드
        # 마지막에는 후위
        

if __name__=="__main__":
    DFS(1)

#중위 순회 연습

#후위 순회 연습