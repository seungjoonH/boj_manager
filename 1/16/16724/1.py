from collections import deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
mp = [input().rstrip() for _ in range(n)]
visited = [[0] * m for _ in range(n)]

DIRS = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}
def out_of_range(r, c): return r not in range(n) or c not in range(m)

count = 0

def travel(r, c):
  if visited[r][c]: return
  global count
  queue = deque([(r, c)])
  routes = {(r, c)}

  while queue:
    cr, cc = queue.popleft()
    visited[cr][cc] = -1

    dr, dc = DIRS[mp[cr][cc]]
    nr, nc = cr + dr, cc + dc
    if out_of_range(nr, nc): continue
    next_value = visited[nr][nc]
    if not next_value: 
      queue.append((nr, nc))
      routes.add((nr, nc))
    else:
      fill = 0
      if next_value > 0: fill = next_value
      else: fill = count + 1; count += 1
      for tr, tc in routes: visited[tr][tc] = fill

for i in range(n):
  for j in range(m):
    if visited[i][j]: continue
    travel(i, j)

print(count)