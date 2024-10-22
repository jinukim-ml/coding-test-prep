# 셔틀버스 https://school.programmers.co.kr/learn/courses/30/lessons/17678
from datetime import datetime, timedelta
from collections import deque
def solution(n, t, m, timetable):
    # Bus timetable
    busses = [datetime.strptime('09:00', '%H:%M')]
    for _ in range(n-1):
        next_bus = busses[-1] + timedelta(minutes=t)
        busses.append(next_bus)

    # Convert crew timetable
    for idx, time_str in enumerate(timetable):
        time_str = datetime.strptime(time_str, '%H:%M')
        timetable[idx] = time_str

    timetable = deque(sorted(timetable))

    for bus_time in busses: # Loop through each bus
        seats = m # Available seats for each bus
        while timetable and timetable[0] <= bus_time and seats > 0:
            seats -= 1
            last_crew = timetable.popleft()

    if seats > 0:
        answer = busses[-1]
    else:
        answer = last_crew - timedelta(minutes=1)

    answer = answer.strftime("%H:%M")
    return answer