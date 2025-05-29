from sys import stdin
input = stdin.readline

for i in range(int(input())):
  n = int(input())
  stickers = [list(map(int, input().split()))]
  stickers += [list(map(int, input().split()))]

  dp = [[0, 0, 0] for _ in range(n)]
  dp[0] = [0, stickers[0][0], stickers[1][0]]

  for i in range(n - 1):
    dp[i + 1][0] = max(dp[i])
    dp[i + 1][1] = max(dp[i][0], dp[i][2]) + stickers[0][i + 1]
    dp[i + 1][2] = max(dp[i][0], dp[i][1]) + stickers[1][i + 1]

  print(max(dp[-1]))