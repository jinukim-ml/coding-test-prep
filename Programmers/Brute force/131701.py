'''
Solution for https://school.programmers.co.kr/learn/courses/30/lessons/131701
'''

def solution(elements):
    n = len(elements)
    answer_set = set(elements)

    prefixSums = [elements[0]]
    for i in range(1,len(elements)):
        prefixSums.append(elements[i] + prefixSums[i-1])

    for i in range(len(elements)):
        if i == 0: # Subsequence length is 1
                answer_set = set(elements)
                continue
        if i == len(elements)-1:
             answer_set.add(prefixSums[-1])
             break
        for j in range(i, i+len(elements)): # Subsequence length 2 ~ n
            if j == i:
                 answer_set.add(prefixSums[j])
                 continue
            val = prefixSums[j%n] - prefixSums[j-(i+1)]
            if val < 0:
                val += prefixSums[-1] # Adjustment
            answer_set.add(val)

    return len(answer_set)

# Much, much better answer (not mine but now I understand this code)
def solution2(elements):
    n = len(elements)
    answer_set = set()

    for i in range(n):
        pivot = elements[i]
        answer_set.add(pivot)
        for j in range(i+1, i+n):
            pivot += elements[j%n]
            answer_set.add(pivot)

    return len(answer_set)