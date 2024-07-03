from functools import cache

# solution 1 (backtracking)

n = int(input())
t, p = [], []
for i in range(n):
    ti, pi = map(int, input().split())
    t.append(ti)
    p.append(pi)

@cache
def backtrack(i:int, profit:int) -> int:
    if i >= n:
        return profit
    
    if i + t[i] <= n:
        return max(backtrack(i+t[i], profit + p[i]), backtrack(i+1, profit))
    else:
        return backtrack(i+1, profit)

print(backtrack(0, 0))

# solution 2 (bottom-up DP)

n = int(input())
t, p = [], []
for i in range(n):
    ti, pi = map(int, input().split())
    t.append(ti)
    p.append(pi)

dp = [0] * (n+1)
for i in range(n-1, -1, -1):
    if i + t[i] <= n:
        dp[i] += max(dp[i+t[i]] + p[i], dp[i+1])
    else:
        dp[i] += dp[i+1]

print(dp[0])