# 맞았습니다!!
# https://www.acmicpc.net/source/66019243

from sys import stdin
input = stdin.readline

n = int(input())
min_dp = [0, 0, 0]
max_dp = [0, 0, 0]

for i in range(n):
  ipts = list(map(int, input().split(' ')))
  min_tp = min_dp[:]
  max_tp = max_dp[:]

  for j in range(3):
    f = max(0, j - 1)
    t = min(2, j + 1) + 1
    min_dp[j] = min(min_tp[f:t]) + ipts[j]
    max_dp[j] = max(max_tp[f:t]) + ipts[j]

print(max(max_dp), min(min_dp))