from sys import stdin
input = stdin.readline

n = int(input())
points = [int(input()) for _ in range(n)]
dp = [0] * n

dp[0] = points[0]
if n > 1: dp[1] = points[0] + points[1]

for i in range(2, n):
  dp[i] = max(dp[i - 2], dp[i - 3] + points[i - 1]) + points[i]

print(dp[-1])

# 10 20 14 25 10 20
# 10 30