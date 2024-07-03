import sys
readline = sys.stdin.readline

for _ in range(3):
    trial = list(map(int, readline().split()))

    if sum(trial) == 4:
        print('E')
    elif sum(trial) == 0:
        print('D')
    elif sum(trial) == 1:
        print('C')
    elif sum(trial) == 2:
        print('B')
    elif sum(trial) == 3:
        print('A')