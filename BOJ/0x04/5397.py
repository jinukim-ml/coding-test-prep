import sys

MX = 1000001
dat = [0]*MX
pre = [-1]*MX
nxt = [-1]*MX
unused = 1

def traverse():
    cur = nxt[0]
    while(cur != -1):
        sys.stdout.write(dat[cur])
        # print(dat[cur], end='')
        cur = nxt[cur]
    sys.stdout.write('\n')

def insert(addr, num):
    global unused
    dat[unused] = num
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

n = int(sys.stdin.readline().strip())
for _ in range(n):
    string = sys.stdin.readline().strip()
    cursor = 0
    nxt[0] = -1
    unused = 1
    for idx, char in enumerate(string):
        if char == '<':
            if pre[cursor] != -1:
                cursor = pre[cursor]
        elif char == '>':
            if nxt[cursor] != -1:
                cursor = nxt[cursor]
        elif char == '-':
            if pre[cursor] != -1:
                erase(cursor)
                cursor = pre[cursor]
        else:
            insert(cursor, char)
            cursor = nxt[cursor]
    traverse()