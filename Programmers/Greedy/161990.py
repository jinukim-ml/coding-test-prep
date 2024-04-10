'''
Solution for https://school.programmers.co.kr/learn/courses/30/lessons/161990
Type: Graph
'''

# 28 days in a month -> 28*12 = 336 days in a year
def solution(wallpaper):
    m, n = len(wallpaper), len(wallpaper[0])
    up, down, left, right = m+1, 0, n+1, 0

    for i in range(m):
        for j in range(n):
            if wallpaper[i][j] == '#':
                if up > i:
                    up = i
                if down <= i:
                    down = i+1
                if left > j:
                    left = j
                if right <= j:
                    right = j+1

    return [up, left, down, right]