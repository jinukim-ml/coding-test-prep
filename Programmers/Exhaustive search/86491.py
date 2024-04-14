'''
Solution for https://school.programmers.co.kr/learn/courses/30/lessons/86491
Type: Exhaustive search
'''
def solution(sizes):
    width = []
    height = []
    for i in range(len(sizes)):
        width.append(sizes[i][0])
        height.append(sizes[i][1])

    max_width = max(width)
    max_height = max(height)

    if max_width >= max_height:
        orientation = 0
    else:
        orientation = 1
    
    for i in range(len(sizes)):
        if sizes[i][orientation] == max(width[i], height[i]):
            continue
        else:
            width[i], height[i] = height[i], width[i]

    return max(width)*max(height)