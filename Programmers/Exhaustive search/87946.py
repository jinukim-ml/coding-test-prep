'''
Solution for https://school.programmers.co.kr/learn/courses/30/lessons/87946
Type: Exhaustive search
'''
def search(k, dungeons, visited, prev_visits):
    max_visits = 0
    for i in range(len(dungeons)):
        if visited[i] or k < dungeons[i][0]:
            continue
        k -= dungeons[i][1]
        visited[i] = True
        
        num_visits = search(k, dungeons, visited, prev_visits+1)
        if max_visits < num_visits:
            max_visits = num_visits

        k += dungeons[i][1]
        visited[i] = False
    
    return max(sum(visited), max_visits)

def solution(k, dungeons):
    answer = []
    visited = [False] * len(dungeons)
    for i in range(len(dungeons)): # Search one by one
        if k < dungeons[i][0]:
            continue
        k -= dungeons[i][1]
        visited[i] = True
        answer.append(search(k, dungeons, visited, 1))

        k += dungeons[i][1]
        visited[i] = False
    
    return max(answer)