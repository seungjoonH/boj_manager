from collections import deque
from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
_map = [[int(x) for x in input().strip()] for _ in range(n)]
_visited = [[[0, _map[r][c]] for c in range(m)] for r in range(n)]

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
in_bound = lambda r, c: 0 <= r < n and 0 <= c < m
dir = lambda r, c: [(r + dr, c + dc) for dr, dc in dirs if in_bound(r + dr, c + dc)]
is_last = lambda r, c: r == n - 1 and c == m - 1

queue = deque([(0, 0)])
_visited[0][0] = [1, 0]

while queue:
  curr_row, curr_col = queue.popleft()
  curr_visited, curr_broke = _visited[curr_row][curr_col]
  next_visited = curr_visited + 1

  for next_row, next_col in dir(curr_row, curr_col):
    next_wall = _map[next_row][next_col]
    next_origin_visited, next_broke = _visited[next_row][next_col]

    if curr_broke and next_broke: continue
    elif curr_broke and not next_broke:
      next_broke = 1
      if next_origin_visited: continue
      else: next_new_visited = next_visited
    elif not curr_broke and next_broke:
      if next_origin_visited: 
        if next_wall: continue
        next_broke = 0
      else: next_broke = 1
      next_new_visited = next_visited
    else:
      next_broke = 0
      if next_origin_visited: continue
      else: next_new_visited = next_visited

    if next_origin_visited > 0 and is_last(next_row, next_col):
      next_new_visited = min(next_origin_visited, next_new_visited)
    _visited[next_row][next_col] = [next_new_visited, next_broke]

    next_element = (next_row, next_col)
    if next_element not in queue: queue.append(next_element)

print(_visited[-1][-1][0] or -1)