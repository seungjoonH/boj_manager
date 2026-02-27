t, *a = [*map(int, open(0))]
dp = [1, 1, 1, 2, 2]
for i in range(max(a) - 5): dp.append(dp[i] + dp[i + 4])
for i in a: print(dp[i - 1])