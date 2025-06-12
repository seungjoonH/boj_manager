from sys import stdin
input = stdin.readline

INF = float('inf')
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
r_most = 2 ** (n - 1)
dp = [[0] * r_most for _ in range(n)]

for i in range(n):
  for j in range(n):
    if i == j or graph[i][j]: continue
    graph[i][j] = INF

def to_set(b): return {i for i in range(1, n) if b & (1 << (i - 1))}
def to_bitmask(s):
  n = 0
  for v in s: n |= 1 << (v - 1)
  return n

for j in range(r_most):
  j_set = to_set(j)
  for i in range(n):
    if not j: dp[i][0] = graph[i][0]; continue
    if not i and j < r_most - 1: continue
    if i in j_set: continue
    dp[i][j] = min(graph[i][v] + dp[v][to_bitmask(j_set - set([i, v]))] for v in j_set)

print(dp[0][-1])