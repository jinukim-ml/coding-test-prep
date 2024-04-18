'''
Solution for https://school.programmers.co.kr/learn/courses/30/lessons/12909
Type: Stack
'''
from collections import deque
def solution(s):
    stack = deque()
    for p in s:
        
        if p == '(':
            stack.append(p)
        else:
            try:
                stack.pop()
            except:
                return False
        # print(stack)

    if stack:
        return False
    else:
        return True