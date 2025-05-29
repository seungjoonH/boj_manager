s1, s2 = input(), input()
l1, l2 = map(len, [s1, s2])

dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
mx = 0
for i in range(l1):
  for j in range(l2):
    if s1[i] == s2[j]: 
      dp[i + 1][j + 1] = dp[i][j] + 1
      mx = max(mx, dp[i][j] + 1)
      continue
    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

print(mx)