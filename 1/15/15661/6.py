from sys import stdin
input = stdin.readline

n = int(input())
powers = [[*map(int, input().split())] for _ in range(n)]

for i in range(n):
  for j in range(i + 1, n):
    powers[i][j] = powers[j][i] = powers[i][j] + powers[j][i]

size = 1 << n
dp = [0] * size

for i in range(1, size):
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

for mask in range(1, size - 1):
  if not (mask & 1): continue
  other = (size - 1) ^ mask
  minimum = min(minimum, abs(dp[mask] - dp[other]))

print(minimum)