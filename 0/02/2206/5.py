from collections import deque
from sys import stdin
input = stdin.readline

make = lambda mat: [[*map(lambda r: [r, 0], row)] for row in mat]

n, m = map(int, input().split())
_map = [[-int(x) for x in input().strip()] for _ in range(n)]
_route = make(_map)

queue = deque([(0, 0, 1, 0)])
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dir = lambda r, c: [(r + dr, c + dc) for dr, dc in dirs]
out_of_bound = lambda r, c: r not in range(n) or c not in range(m)

def move():
  while queue:
    curr_row, curr_col, count, broke = queue.popleft()

    anchor_value, anchor_broke = _route[curr_row][curr_col]

    if anchor_value > 0:
      if broke == anchor_broke:
        if anchor_value <= count: continue
      elif broke > anchor_broke: continue

      if (curr_row, curr_col) == (n - 1, m - 1): 
        count = min(count, anchor_value)

    _route[curr_row][curr_col] = [count, broke]

    for next_row, next_col in dir(curr_row, curr_col):
      if out_of_bound(next_row, next_col): continue
      if _map[next_row][next_col] < 0 and broke: continue

      anchor_value, anchor_broke = _route[next_row][next_col]

      if anchor_value > 0:
        if broke == anchor_broke:
          if anchor_value <= count: continue
        elif broke > anchor_broke: continue

      next_count = count + 1
      next_broke = broke - _map[next_row][next_col]
      queue.append((next_row, next_col, next_count, next_broke))

move()
print(_route[-1][-1][0] or -1)