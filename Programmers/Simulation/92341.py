'''
Solution for https://school.programmers.co.kr/learn/courses/30/lessons/92341
Type: Simulation
'''
from math import ceil
def solution(fees, records):
    cumulativetime = {}
    parked = {}

    # cumulative time calculation
    # fee according to cumulative time

    for r in records:
        time, car, stat = r.split()
        time = int(time[:2])*60 + int(time[3:])
        if stat == 'IN':
            parked[car] = time
        else: # stat == 'OUT'
            parkedtime = time - parked[car]
            cumulativetime[car] = cumulativetime.get(car, 0) + parkedtime
            parked.pop(car) # remove car from the parking lot
    
    endofday = 1439
    for car in parked:
        cumulativetime[car] = endofday - parked[car] + cumulativetime.get(car, 0)
    
    answer = []
    for car in sorted(cumulativetime.keys()):
        fee = fees[1] + ceil((cumulativetime[car] - fees[0])/fees[2]) * fees[3] * (cumulativetime[car] - fees[0] > 0)
        answer.append(fee)
    
    return answer