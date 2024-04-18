'''
Solution for https://school.programmers.co.kr/learn/courses/30/lessons/131704
Type: Stack
'''
from collections import deque
def solution(order):
    answer = 0
    stack = deque()
    
    for i in range(1, len(order)+1):
        stack.append(i)
        
        while stack and stack[-1] == order[answer]:
            stack.pop()
            answer += 1
    return answer