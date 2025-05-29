from collections import deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
_map = [[int(x) for x in input().strip()] for _ in range(n)]
_visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
in_bound = lambda r, c: 0 <= r < n and 0 <= c < m
dir = lambda r, c: [(r + dr, c + dc) for dr, dc in dirs if in_bound(r + dr, c + dc)]
is_last = lambda r, c: r == n - 1 and c == m - 1

sx, sy, sz = 0, 0, 0
_visited[sx][sy][sz] = 1
queue = deque([(sx, sy, sz)])

def move():
  while queue:
    curr_row, curr_col, broke = queue.popleft()
    if is_last(curr_row, curr_col): break

    for next_row, next_col in dir(curr_row, curr_col):
      is_next_wall = _map[next_row][next_col]
      next_broke = 0

      if is_next_wall:
        if broke: continue
        _visited[next_row][next_col][1] = _visited[curr_row][curr_col][0] + 1
        next_broke = 1
      else:
        if _visited[next_row][next_col][broke]: continue
        _visited[next_row][next_col][broke] = _visited[curr_row][curr_col][broke] + 1
        next_broke = broke

      queue.append((next_row, next_col, next_broke))

move()
print(_visited[-1][-1][-1] or -1)