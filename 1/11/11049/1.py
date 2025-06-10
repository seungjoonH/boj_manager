from sys import stdin
input = stdin.readline

n = int(input())
p = [int(input().split()[0]) for _ in range(n - 1)]
p.extend(map(int, input().split()))

dp = [[0] * n for _ in range(n)]
for i in range(n - 1): dp[i][i + 1] = p[i] * p[i + 1] * p[i + 2]
for i in range(2, n):
  for j in range(n - i):
    left, right = j, i + j
    dp[left][right] = min(
      dp[left][mid] + dp[mid + 1][right] + p[left] * p[mid + 1] * p[right + 1]
      for mid in range(left, right)
    )

print(dp[0][-1])