from collections import defaultdict

def solution(friends, gifts):
    max_result = 0
    gift_dict = {
        friend: {
            'count': 0,  # 선물 횟수
            **{f: 0 for f in friends}  # 친구마다 선물 횟수 초기화
        }
        for friend in friends
    }

    for gift in gifts:
        a,b = gift.split(' ')
        gift_dict[a]['count'] +=1
        gift_dict[a][b] += 1
        gift_dict[b]['count'] -= 1
    
    for f1 in friends:
        result = 0
        for f2 in friends:
            if gift_dict[f1][f2] > gift_dict[f2][f1]:
                result += 1
            elif gift_dict[f1][f2] == gift_dict[f2][f1]:
                if gift_dict[f1]['count'] > gift_dict[f2]['count']:
                    result+=1
        max_result = max(max_result, result)
    
    return max_result


friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
result= 2

solution(friends, gifts)

