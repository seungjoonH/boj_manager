# 
# 89256996

from sys import stdin
input = stdin.readline

(n, m), map_ = map(int, input().split()), []

WALL, ROUTE, TARGET = '012'
DIRS = (1, 0), (0, 1), (-1, 0), (0, -1)
target = -1, -1

def out_of_range(r, c): return r not in range(n) or c not in range(m)
def is_int(v): return type(v) is int

for i in range(n):
  row = input().split()
  if TARGET in row: target = i, row.index(TARGET)
  map_.append(row)

queue = {target: 0}

while queue:
  next_queue = dict()

  for (r, c), dist in queue.items():
    map_[r][c] = dist

    for dr, dc in DIRS:
      nr, nc = r + dr, c + dc
      if out_of_range(nr, nc): continue
      nv = map_[nr][nc]
      if is_int(nv): continue
      if nv == WALL: continue
      next_queue[(nr, nc)] = dist + 1
  
  queue = next_queue

for row in map_:
  print(*[int(i) * (2 * is_int(i) - 1) for i in row])