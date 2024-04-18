'''
Solution for https://school.programmers.co.kr/learn/courses/30/lessons/154539
Type: Stack
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

    for i in range(n):
        while len(stack) > 0 and numbers[stack[-1]] < numbers[i]:
            idx = stack.pop()
            answer[idx] = numbers[i]
        stack.append(i) # push
    return answer