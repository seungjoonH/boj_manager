n, a = int(input()), [*map(int, input().split())]
g = {i: set() for i in range(-1, n)}
for i, v in enumerate(a): g[v].add(i)

dp = [0] * n
for i in range(n - 1, -1, -1):
  if not len(g[i]): continue
  s = sorted(map(lambda x: dp[x], g[i]))[::-1]
  dp[i] = max(1 + v + j for j, v in enumerate(s))

print(dp[0])