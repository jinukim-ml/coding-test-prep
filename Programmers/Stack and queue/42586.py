'''
Solution for https://school.programmers.co.kr/learn/courses/30/lessons/42586
Type: Queue
'''
from collections import deque
from math import ceil
def solution(progresses, speeds):
    q = deque()
    for i in range(len(progresses)):
        q.append(ceil((100-progresses[i])/speeds[i]))

    answer = [0]
    bottleneck = q[0]
    idx = 0

    while q:
        date = q.popleft()
        if bottleneck >= date:
            answer[idx] += 1
        else:
            answer.append(1)
            bottleneck = date
            idx += 1
    return answer