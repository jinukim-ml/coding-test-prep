'''
N-Queen (https://www.acmicpc.net/problem/9663)
Difficulty: Gold-IV
'''

n = int(input())
col = set()
posdiag = set() # r + c
negdiag = set() # r - c

ans = 0
def backtrack(r):
    global ans
    if r == n:
        ans += 1
        return
    
    for c in range(n):
        if c in col or (r+c) in posdiag or (r-c) in negdiag:
            continue
        
        col.add(c)
        posdiag.add(r+c)
        negdiag.add(r-c)
        backtrack(r+1)

        col.remove(c)
        posdiag.remove(r+c)
        negdiag.remove(r-c)

backtrack(0)
print(ans)