from sys import stdin
input = stdin.readline

INF = float('inf')

insts = list(map(int, input().split()))[:-1]
n = len(insts)
dp = [[[INF] * 5 for _ in range(5)] for _ in range(n + 1)]
dp[0][0][0] = 0

def get_force(bef, aft):
  if not bef: return 2
  elif bef == aft: return 1
  elif abs(bef - aft) == 2: return 4
  return 3

for i in range(n):
  nxt = insts[i]
  for l in range(5):
    for r in range(5):
      value = dp[i][l][r]
      if value == INF: continue
      dp[i + 1][nxt][r] = min(dp[i + 1][nxt][r], value + get_force(l, nxt))
      dp[i + 1][l][nxt] = min(dp[i + 1][l][nxt], value + get_force(r, nxt))

print(min(map(min, dp[-1])))