MOD = 10 ** 9

n = int(input())
dp = [[[0] * (1 << 10) for _ in range(10)] for __ in range(n + 1)]

for j in range(1, 10): dp[1][j][1 << j] = 1
for i in range(2, n + 1):
  for j in range(10):
    for k in range(1 << 10):
      lj, rj, nk = j - 1, j + 1, k | (1 << j)
      l = lj >= 0 and dp[i - 1][lj][k]
      r = rj <= 9 and dp[i - 1][rj][k]
      dp[i][j][nk] += l + r
      dp[i][j][nk] %= MOD

print(sum([dp[n][j][(1 << 10) - 1] for j in range(10)]) % MOD)