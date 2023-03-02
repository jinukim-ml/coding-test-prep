import sys

MX = 1000001
dat = [0]*MX
pre = [-1]*MX
nxt = [-1]*MX
unused = 1

def print_arr(arr):
    for _, elem in enumerate(arr):
        print(elem, end=' ')

def traverse():
    cur = nxt[0]
    while(cur != -1):
        print(dat[cur], end='')
        cur = nxt[cur]
    print()

def insert(addr: int, data: str):
    global unused
    dat[unused] = data
    pre[unused] = addr
    nxt[unused] = nxt[addr]

    if nxt[addr] != -1: pre[nxt[addr]] = unused
    nxt[addr] = unused

    unused += 1

def erase(addr: int):
    # previous = pre[addr]
    # next = nxt[addr]
    nxt[pre[addr]] = nxt[addr]
    if nxt[addr] != -1: pre[nxt[addr]] = pre[addr]

string = list(sys.stdin.readline().strip())
for idx, num in enumerate(string):
    insert(idx, num)

n = int(sys.stdin.readline().strip())
cursor = unused-1

for _ in range(n):
    command = sys.stdin.readline().strip().split()

    if command[0] == 'L' and pre[cursor] != -1:
        cursor = pre[cursor]
    elif command[0] == 'D' and nxt[cursor] != -1:
        cursor = nxt[cursor]
    elif command[0] == 'B' and pre[cursor] != -1:
        erase(cursor)
        cursor = pre[cursor]
    elif command[0] == 'P':
        insert(cursor, command[1])
        cursor = nxt[cursor]
traverse()