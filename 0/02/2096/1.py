# 메모리 초과
# https://www.acmicpc.net/source/66018295

n = int(input())
board = [list(map(int, input().split(' '))) for i in range(n)]
min_dp = [[0, 0, 0] for _ in range(n)]
max_dp = [[0, 0, 0] for _ in range(n)]

def upper_list(dp, x, y):
  l = []
  if x == 0: return [0]
  l.append(dp[x - 1][y])
  if y > 0: l.append(dp[x - 1][y - 1])
  if y < 2: l.append(dp[x - 1][y + 1])
  return l

for i in range(n):
  for j in range(3):
    cur = board[i][j]
    min_dp[i][j] = min(upper_list(min_dp, i, j)) + cur
    max_dp[i][j] = max(upper_list(max_dp, i, j)) + cur
    
print(max(max_dp[-1]), min(min_dp[-1]))