'''
Solution for https://school.programmers.co.kr/learn/courses/30/lessons/17678
Kakao blind recruitment 2018
A simulation problem
'''
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

    if seats > 0: # There are available seats -> get in line when the last bus arrives.
        answer = busses[-1]
    else: # No seats on the last bus -> arrive 1 minute earlier than the last crew
        answer = last_crew - timedelta(minutes=1)

    answer = answer.strftime("%H:%M")
    return answer