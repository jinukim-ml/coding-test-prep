'''
Solution for https://school.programmers.co.kr/learn/courses/30/lessons/181187
Type: Math
'''
import math
def solution(r1, r2):
    answer = 0 

    for x in range(1, r2+1):
        y1 = (r1**2 - x**2)**0.5
        y2 = (r2**2 - x**2)**0.5

        if x < r1:
            start = math.ceil(y1)
        else:
            start = 0
        
        end = int(y2)

        answer += end - start + 1
    return answer*4