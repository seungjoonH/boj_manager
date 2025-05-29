from sys import stdin

input = stdin.readline
INF = 2e9

graph = []
def bellman_ford(s):
  table = [INF] * n
  table[s] = 0

  for i in range(n):
    for edge in graph:
      curr, next, cost = edge
      before = table[next]
      table[next] = min(table[next], table[curr] + cost)
      if i == n - 1 and before != table[next]: 
        return True
  
  return False

for _ in range(int(input())):
  n, m, w = map(int, input().split())
  graph = []

  for i in range(m + w):
    is_road = i < m
    adj = 2 * is_road - 1
    s, e, t = map(int, input().split())
    s -= 1; e -= 1
    
    graph.append((s, e, t * adj))
    if is_road: graph.append((e, s, t * adj))

  print('YES' if bellman_ford(0) else 'NO')