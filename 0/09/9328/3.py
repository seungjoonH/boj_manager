from sys import stdin
from collections import deque

input = stdin.readline

WALL, VOID, DOCS = '*.$'
DIRS = (1, 0), (0, 1), (-1, 0), (0, -1)

def is_door(c): return 'A' <= c <= 'Z'
def is_key(c): return 'a' <= c <= 'z'

def testcase():
  h, w = map(int, input().split())
  
  mp = [list(input().rstrip()) for _ in range(h)]
  key_ipt = input().rstrip()

  padded = [[VOID] * (w + 2)]
  for row in mp: padded.append([VOID] + row + [VOID])
  padded.append([VOID] * (w + 2))
  H, W = h + 2, w + 2

  def out_of_range(r, c): 
    return r not in range(H) or c not in range(W)

  visited = [[0] * W for _ in range(H)]
  keys = set() if key_ipt == '0' else set(key_ipt)

  doors = dict()

  doc_count = 0
  queue = deque()
  queue.append((0, 0))
  visited[0][0] = 1

  while queue:
    r, c = queue.popleft()
    for dr, dc in DIRS:
      nr, nc = r + dr, c + dc
      if out_of_range(nr, nc): continue
      if visited[nr][nc]: continue
      v = padded[nr][nc]
      
      if v == WALL: continue

      if is_door(v):
        if v.lower() in keys:
          visited[nr][nc] = 1
          padded[nr][nc] = VOID
          queue.append((nr, nc))
        else: 
          doors.setdefault(v, set()).add((nr, nc))
        continue

      if is_key(v):
        if v not in keys:
          keys.add(v)
          door = v.upper()
          if door in doors:
            for (drx, dcx) in doors[door]:
              if not visited[drx][dcx]:
                visited[drx][dcx] = 1
                padded[drx][dcx] = VOID
                queue.append((drx, dcx))
            del doors[door]
        visited[nr][nc] = 1
        padded[nr][nc] = VOID
        queue.append((nr, nc))
        continue

      if v == DOCS:
          doc_count += 1
          padded[nr][nc] = VOID

      visited[nr][nc] = 1
      queue.append((nr, nc))

  print(doc_count)

for _ in range(int(input())): testcase()