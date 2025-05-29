from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
  weight, value = map(int, input().split())
  for w in range(1, k + 1):
    if weight > w: dp[i][w] = dp[i - 1][w]; continue
    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)

print(dp[-1][-1])