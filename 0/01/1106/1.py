from sys import stdin
input = stdin.readline

c, n = map(int, input().split())
cities = [0] + [tuple(map(int, input().split())) for _ in range(n)]
dp = [[0] * (n + 1)]
budget = 0

while True:
  budget += 1
  dp.append([0] * (n + 1))
  for i in range(1, n + 1):
    cost, count = cities[i]
    left = dp[budget][i - 1]
    if cost > budget: dp[budget][i] = left
    else: dp[budget][i] = max(left, dp[budget - cost][i] + count)
  if dp[-1][-1] >= c: break

print(budget)