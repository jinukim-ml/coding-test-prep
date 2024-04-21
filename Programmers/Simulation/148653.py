'''
Solution for https://school.programmers.co.kr/learn/courses/30/lessons/148653
Type: Simulation
'''
from collections import Counter
def solution(weights):
    answer = 0
    cnt = Counter(weights)
    for w, c in cnt.items():
        if c >= 2:
            answer += c*(c-1)/2 # c C 2 choices
    
    weights = set(weights)

    for w in weights:
        if w * 2 in weights:
            answer += cnt[w] * cnt[w*2]
        if w * 2/3 in weights:
            answer += cnt[w] * cnt[w*2/3]
        if w * 3/4 in weights:
            answer += cnt[w] * cnt[w*3/4]
    return answer