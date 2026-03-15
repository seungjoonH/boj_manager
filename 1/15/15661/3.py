from sys import stdin
input = stdin.readline

n = int(input())
powers = [[*map(int, input().split())] for _ in range(n)]

for i in range(n):
  for j in range(i + 1, n):
    powers[i][j] = powers[j][i] = powers[i][j] + powers[j][i]

size = 1 << n
dp = [0] * size

for i in range(size - 1):
  lsb = i & -i
  prev = i ^ lsb
  k = lsb.bit_length() - 1
  score = dp[prev] 
  r = prev

  while r:
    b = r & -r
    score += powers[k][b.bit_length() - 1]
    r ^= b

  dp[i] = score

minimum = float('inf')

for i in range(size):
  if i.bit_count() != n // 2: continue
  other = ((1 << n) - 1) ^ i
  minimum = min(minimum, abs(dp[i] - dp[other]))

print(minimum)