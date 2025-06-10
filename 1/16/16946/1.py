from sys import stdin
from copy import deepcopy
from collections import deque

def input(): return stdin.readline().rstrip()

DIRS = (1, 0), (0, 1), (-1, 0), (0, -1)

n, m = map(int, input().split())
mp = [int(input(), 2) for _ in range(n)]

result = [[2 ** (m - i - 1) & row and -1 for i in range(m)] for row in mp]
blanks = deepcopy(result)

def out_of_range(r, c): 
  return r not in range(n) or c not in range(m)

def fill_blanks(l):
  index = 0
  visited = deepcopy(l)

  def bfs(r, c):
    nonlocal index
    if l[r][c]: return

    queue = deque([(r, c)])
    blanks = set()
    count = 0

    while queue:
      cr, cc = queue.popleft()
      visited[cr][cc] = 1
      blanks.add((cr, cc))
      count += 1

      for dr, dc in DIRS:
        nr, nc = cr + dr, cc + dc

        if out_of_range(nr, nc): continue
        if visited[nr][nc]: continue
        visited[nr][nc] = 1

        queue.append((nr, nc))
    
    for r, c in blanks:
      l[r][c] = (count, index)
    
    index += 1

  for i in range(n):
    for j in range(m):
      bfs(i, j)

fill_blanks(blanks)

for i in range(n):
  for j in range(m):
    if result[i][j] >= 0: continue
    
    value = 1
    indices = set()
    for dr, dc in DIRS:
      nr, nc = i + dr, j + dc
      if out_of_range(nr, nc): continue
      if type(blanks[nr][nc]) is int: continue
      count, index = blanks[nr][nc]
      if index in indices: continue
      value += count
      indices.add(index)

    result[i][j] = value

for row in result: 
  print(*map(lambda x: x % 10, row), sep='')