import sys

MX = 100000
dat = [0]*MX
pre = [-1]*MX
nxt = [-1]*MX
unused = 1

def traverse():
    cur = nxt[0]
    while(cur != -1):
        print(dat[cur], end='')
        cur = nxt[cur]
    print()

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