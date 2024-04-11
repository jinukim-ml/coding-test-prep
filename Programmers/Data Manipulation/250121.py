'''
Solution for https://school.programmers.co.kr/learn/courses/30/lessons/250121
Type: Data manipulation
'''

# 28 days in a month -> 28*12 = 336 days in a year
def solution(data, ext, val_ext, sort_by):
    candidate = []
    ext_code = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    for i in range(len(data)):
        if data[i][ext_code[ext]] < val_ext:
            candidate.append(data[i])
    
    return sorted(candidate, key=lambda item: item[ext_code[sort_by]])