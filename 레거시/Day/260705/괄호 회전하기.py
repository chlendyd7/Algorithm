'''
)]}를 만났을 때 
[ 넣고 ] pop
[( 이렇게 ) pop이 )이면 ok 아니면 바로 x

이건 ok 근데 회전을 어떻게 시킬 것 인가?
[( )]
1000번?
시뮬레이션?

0이면 lst[:0] + lst[0:]
'''
def solution(s):
    def simulation(lst):
        tmp_lst = []
        for l in lst:
            if l == ')':
                if not tmp_lst or tmp_lst.pop() != '(':
                    return 0
            elif l == '}':
                if not tmp_lst or tmp_lst.pop() != '{':
                    return 0
            elif l == ']':
                if not tmp_lst or tmp_lst.pop() != '[':
                    return 0
            else:
                tmp_lst.append(l)
        return 1 if not tmp_lst else 0
    
    cnt = 0
    for i in range(len(s)):
        cnt += simulation(s[i:] + s[:i])
    
    return cnt


def solution(s):
    n = len(s)
    # 연결된 괄호 (예: "[](){}" -> "[](){}[](){}")
    # 이렇게 하면 s[i:i+n]을 통해 회전한 효과를 낼 수 있음
    s_double = s + s
    
    def is_valid(start_idx):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for i in range(start_idx, start_idx + n):
            char = s_double[i]
            if char in mapping.values(): # 여는 괄호
                stack.append(char)
            else: # 닫는 괄호
                if not stack or stack.pop() != mapping[char]:
                    return False
        return not stack

    cnt = 0
    for i in range(n):
        if is_valid(i):
            cnt += 1
    return cnt
