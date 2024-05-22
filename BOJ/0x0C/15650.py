'''
https://www.acmicpc.net/problem/15650
Difficulty: Silver III
'''

n, m = map(int, input().split())
subarray = []
def backtrack(i):
    if len(subarray) == m:
        print(*subarray)
        return
    
    if i == n:
        return
    
    subarray.append(i+1)
    backtrack(i+1)
    subarray.pop()

    backtrack(i+1)

backtrack(0)