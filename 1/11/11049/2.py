from sys import stdin
input = stdin.readline

n = int(input())
p = [int(input().split()[0]) for _ in range(n - 1)]
p.extend(map(int, input().split()))

dp = [[0] * n for _ in range(n)]
def set_dp(r, c, v): dp[r][c] = dp[c][r] = v

for i in range(1, n):
  for j in range(n - i):
    l, r = j, i + j
    d = p[l] * p[r + 1] 
    m = min(a + b + c * d for a, b, c in zip(dp[l][l:r], dp[r][l + 1:r + 1], p[l + 1:r + 1]))
    set_dp(l, r, m)
    
print(dp[0][-1])