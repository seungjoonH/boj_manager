n = int(input())
children = map(int, input().split())

dp = [0] * (n + 1)
for c in children: dp[c] = dp[c - 1] + 1

print(n - max(dp))