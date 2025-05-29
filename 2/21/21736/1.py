from collections import deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
campus, visited = [], []
iy = ix = person = 0

DIRS = (-1, 0), (1, 0), (0, -1), (0, 1)
def out_of_range(x, y): return y not in range(n) or x not in range(m)

for i in range(n):
  l = list(input())
  campus.append(l)
  visited.append([0] * m)
  try: iy, ix = i, l.index("I")
  except: continue

queue = deque([(ix, iy)])

while queue:
  x, y = queue.popleft()
  visited[y][x] = 1

  for dx, dy in DIRS:
    nx, ny = x + dx, y + dy
    if out_of_range(nx, ny): continue
    elif campus[ny][nx] == 'X': continue
    elif visited[ny][nx]: continue
    visited[ny][nx] = 1
    if campus[ny][nx] == 'P': person += 1
    queue.append((nx, ny))

print(person or 'TT')