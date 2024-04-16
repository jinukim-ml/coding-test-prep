'''
Solution for https://school.programmers.co.kr/learn/courses/30/lessons/118666
Type: Implementation
'''
def solution(survey, choices):
    scales = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for i in range(len(survey)):
        if choices[i] - 4 <= 0:
            scales[survey[i][0]] += abs(choices[i]-4)
        else:
            scales[survey[i][1]] += abs(choices[i]-4)
    
    answer = ''
    if scales['R'] >= scales['T']:
        answer += 'R'
    else:
        answer += 'T'
    if scales['C'] >= scales['F']:
        answer += 'C'
    else:
        answer += 'F'
    if scales['J'] >= scales['M']:
        answer += 'J'
    else:
        answer += 'M'
    if scales['A'] >= scales['N']:
        answer += 'A'
    else:
        answer += 'N'
    return answer