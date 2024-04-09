'''
Solution for https://school.programmers.co.kr/learn/courses/30/lessons/172928
Type: Simulation
'''
def solution(park, routes):
    m, n = len(park), len(park[0])
    for i in range(m):
        for j in range(n):
            if park[i][j] == 'S':
                curr = [i,j]
                break
        else:
            continue
        break # break nested loop

    for route in routes:
        direction, distance = route.split()
        distance = int(distance)
        print(f'route: {route}')
        if direction == 'N':
            candidate_y = curr[0] - distance
            
            if candidate_y < 0 or candidate_y >= m:
                continue

            col = []
            for i in range(1, distance+1):
                col.append(park[curr[0]-i][curr[1]]) # Order doesn't matter as we're just checking if there's an obstacle
            if 'X' in col:
                continue
            curr[0] = candidate_y
        elif direction == 'S':
            candidate_y = curr[0] + distance

            
            if candidate_y < 0 or candidate_y >= m:
                continue
            
            col = []
            for i in range(1, distance+1):
                col.append(park[curr[0]+i][curr[1]]) # Order doesn't matter as we're just checking if there's an obstacle
            if 'X' in col:
                continue
            curr[0] = candidate_y
        elif direction == 'W':
            candidate_x = curr[1] - distance
            if candidate_x < 0 or candidate_x >= n:
                continue
            
            row = []
            for i in range(1, distance+1):
                row.append(park[curr[0]][curr[1]-i]) # Order doesn't matter as we're just checking if there's an obstacle
            if 'X' in row:
                continue
            print(f'row:{row}')
            curr[1] = candidate_x
        elif direction == 'E':
            candidate_x = curr[1] + distance
            if candidate_x < 0 or candidate_x >= n:
                continue

            row = []
            for i in range(1, distance+1):
                row.append(park[curr[0]][curr[1]+i]) # Order doesn't matter as we're just checking if there's an obstacle
            print(f'row:{row}')
            if 'X' in row:
                continue
            curr[1] = candidate_x
        print(f'curr:{curr}')
    return curr