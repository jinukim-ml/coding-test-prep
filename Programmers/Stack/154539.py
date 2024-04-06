'''
Solution for https://school.programmers.co.kr/learn/courses/30/lessons/154539
'''

'''
Q. Why can't we use just a single variable to compare?
A. Using a single variable will result in finding the biggest number in the variable.
'''
from collections import deque
def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = deque()

    for i, curr in enumerate(numbers):
        if len(stack) == 0 or stack[-1][-1] >= curr:
            stack.append((i, curr)) # push
        elif stack[-1][-1] < curr:
            while len(stack) > 0 and stack[-1][-1] < curr:
                idx, _ = stack.pop()
                answer[idx] = curr
            stack.append((i, curr))
    return answer