from collections import deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
_map = [[[int(x), 0, 0] for x in input().strip()] for _ in range(n)]

queue = deque([(0, 0, 1, 0)])
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
in_bound = lambda r, c: 0 <= r < n and 0 <= c < m
dir = lambda r, c: [(r + dr, c + dc) for dr, dc in dirs if in_bound(r + dr, c + dc)]

def move():
  while queue:
    curr_row, curr_col, count, broke = queue.popleft()

    is_wall, anchor_value, anchor_broke = _map[curr_row][curr_col]

    if anchor_value:
      if broke == anchor_broke:
        if anchor_value <= count: continue
      elif broke > anchor_broke: continue

      if (curr_row, curr_col) == (n - 1, m - 1): 
        count = min(count, anchor_value)

    _map[curr_row][curr_col] = [is_wall, count, broke]

    for next_row, next_col in dir(curr_row, curr_col):
      anchor_wall, anchor_value, anchor_broke = _map[next_row][next_col]

      if anchor_wall and broke: continue
      if anchor_value:
        if broke == anchor_broke:
          if anchor_value <= count: continue
        elif broke > anchor_broke: continue

      next_count = count + 1
      next_broke = broke + _map[next_row][next_col][0]
      queue.append((next_row, next_col, next_count, next_broke))

move()
print(_map[-1][-1][1] or -1)