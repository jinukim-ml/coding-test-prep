'''
Solution for https://school.programmers.co.kr/learn/courses/30/lessons/92335
Type: Math
'''
def convert(n, k):
    nums = []
    while n:
        n, r = divmod(n, k)
        nums.append(str(r))
    return ''.join(reversed(nums))

def solution(n, k):
    converted = convert(n, k)
    nums = []
    for num in converted.split('0'):
        if num and num != '1':
            nums.append(int(num))
            
    answer = 0
    for num in nums:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            answer += 1
    return answer