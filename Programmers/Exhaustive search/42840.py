'''
Solution for https://school.programmers.co.kr/learn/courses/30/lessons/42840
Type: Exhaustive search
'''
def solution(answers):
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]

    cnt = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == first[i%len(first)]:
            cnt[0] += 1
        if answers[i] == second[i%len(second)]:
            cnt[1] += 1
        if answers[i] == third[i%len(third)]:
            cnt[2] += 1
    
    maximum = max(cnt)
    answer = []
    for i in range(3):
        if cnt[i] == maximum:
            answer.append(i+1)
    return answer