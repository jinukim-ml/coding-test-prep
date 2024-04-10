'''
Solution for https://school.programmers.co.kr/learn/courses/30/lessons/150370
Type: Implementation
'''
def solution(today, terms, privacies):
    today = list(map(int, today.split('.')))
    today = today[0]*336 + (today[1])*28 + today[2]
    tos_book = {}
    for term in terms:
        tos_type, expiry = term.split()
        tos_book[tos_type] = int(expiry)

    answer = []
    for i in range(len(privacies)):
        date, tos_type = privacies[i].split()
        date = list(map(int, date.split('.')))
        date = date[0]*336 + (date[1])*28 + date[2]
        expiry = tos_book[tos_type]

        if today - date > expiry*28-1:
            answer.append(i+1)
    return answer