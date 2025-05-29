from collections import deque
from sys import stdin

input = stdin.readline
row, col = map(int, input().split())
route = [[-int(p == 'W') for p in input()] for _ in range(row)]

copy = lambda mat: [row[:] for row in mat]
out_of_bound = lambda r, c: r not in range(row) or c not in range(col)
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
get_dirs = lambda x, y: [(x + dx, y + dy) for dx, dy in dirs]

def get_wall_count(visited, y, x):
  count = 0
  for _x, _y in get_dirs(x, y):
    count += int(out_of_bound(_y, _x) or visited[_y][_x] != 0)
  return count

def find_farthest(y, x):
  maximum = 0

  def search(sy, sx, check):
    nonlocal maximum
    dq = deque([(sy, sx, 1)])
    
    while dq:
      y, x, level = dq.popleft()
      check[y][x] = level
      maximum = max(maximum, level)

      for _x, _y in get_dirs(x, y):
        if out_of_bound(_y, _x): continue 
        _next = check[_y][_x]
        if _next < 0: continue
        if any((_y, _x) == item[:2] for item in dq): continue
        elif not _next: dq.append((_y, _x, level + 1))

  visited = copy(route)
  search(y, x, visited)

  return maximum - 1

maximum = max_wall_count = 0

for r in range(row):
  for c in range(col):
    if route[r][c]: continue
    wall_count = get_wall_count(route, r, c)
    if wall_count == 4: continue
    if wall_count < max_wall_count: continue
    max_wall_count = max(wall_count, max_wall_count)
    maximum = max(find_farthest(r, c), maximum)

print(maximum)


