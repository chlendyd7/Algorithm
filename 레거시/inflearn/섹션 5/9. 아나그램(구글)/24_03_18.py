'''
    알파뱃 일치?
    dict 사용
'''

first_word = input()
second_word = input()

first_dict = dict()
second_dict = dict()

for f in first_word:
    first_dict[f] = first_dict.get(f,0)+1

for s in second_word:
    second_dict[s] = second_dict.get(s,0)+1

for val in first_dict:
    print(first_dict[val])
#     if key in second_dict.keys():
#         if first_dict[key] != second_dict[key]:
#             print("NO")
#             break
#     else:
#         print("NO")
# else:
#     print("YES")
