from collections import deque
from sys import stdin
input = stdin.readline

BLANK, WALL = '10'
DIRS = (1, 0), (0, 1), (-1, 0), (0, -1)

n, m = map(int, input().split())
maze = [[*input().strip()] for _ in range(n)]
visited = set()

dq = deque([(0, 0, 1)])
maze[0][0] = 1

while dq:
  r, c, count = dq.popleft()

  for dr, dc in DIRS:
    nr, nc = r + dr, c + dc
    if not (0 <= nr < n): continue
    if not (0 <= nc < m): continue
    if maze[nr][nc] == WALL: continue
    if type(maze[nr][nc]) is int: continue

    dq.append((nr, nc, count + 1))
    maze[nr][nc] = count + 1

    if nr == n and nc == m: break

print(maze[-1][-1])