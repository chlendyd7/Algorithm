from string import ascii_lowercase

def solution(s, skip, index):
    a_to_z = set(ascii_lowercase)
    a_to_z -= set(skip)
    a_to_z = sorted(a_to_z)
    l = len(a_to_z)
    
    a_to_z_dict =  {
        alpha : idx for idx, alpha in enumerate(a_to_z)
    }
    answer = ''
    for a in s:
        answer+= a_to_z[(a_to_z_dict[a] + index) % l]
        
    return answer
