'''
Solution for https://school.programmers.co.kr/learn/courses/30/lessons/132265
Type: Etc
'''
def solution(topping):
    answer = 0
    n = len(topping)

    topping_counts = {}
    for i in range(n):
        topping_counts[topping[i]] = topping_counts.get(topping[i], 0) + 1

    left_unique_count = 0
    left_counts = {}

    for i, t in enumerate(topping):
        left_counts[t] = left_counts.get(t, 0) + 1
        if left_counts[t] == 1:
            left_unique_count += 1
        
        topping_counts[t] -= 1
        if topping_counts[t] == 0:
            topping_counts.pop(t, None)

        if left_unique_count == len(topping_counts):
            answer += 1

    return answer