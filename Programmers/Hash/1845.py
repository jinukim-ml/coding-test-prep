'''
Solution for https://school.programmers.co.kr/learn/courses/30/lessons/1845
Hash problem
'''
def solution(nums):
    unique = set(nums)
    unique_num = len(unique)

    if unique_num >= len(nums)/2:
        return int(len(nums)/2)
    else:
        return unique_num