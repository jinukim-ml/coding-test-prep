'''
Solution for https://school.programmers.co.kr/learn/courses/30/lessons/140107
'''
# Key idea: only iterate over x coordinates.
# This makes the time complexity O(n).

def solution(k, d):
    answer = 0
    q = d//k

    for x in range(0, q+1):
        y = (d**2 - (x * k)**2)**(1/2)
        answer += y//k + 1
        # if y == int(y) and y % k == 0: # On the quarter circle
            # answer += 1
        
    return int(answer)