from collections import deque
from sys import stdin
input = stdin.readline

BLANK, WALL, S, FIRE, EXIT = '.#@* '
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def build(w, h, structure):
  building = [[(EXIT, 1)] * (w + 2) for _ in range(h + 2)]
  coords = { S: (0, 0), FIRE: [] }

  for r in range(h):
    for c in range(w):
      cell = structure[r][c]
      if cell == S: coords[S] = (r + 1, c + 1)
      elif cell == FIRE: coords[FIRE].append((r + 1, c + 1))

      building[r + 1][c + 1] = (structure[r][c], 1)

  return building, coords


def test(w, h, structure):
  building, coords = build(w, h, structure)
  
  init = *coords[FIRE], coords[S]
  dq = deque(init)
  dqset = set(init)
  
  while dq:
    r, c = dq.popleft()
    dqset.remove((r, c))

    curr, count = building[r][c]
    if curr[0] not in [S, FIRE]: continue

    for dr, dc in DIRS:
      nr, nc = r + dr, c + dc
      if not (0 <= nr < h + 2 and 0 <= nc < w + 2): continue
      next, _ = building[nr][nc]

      if next == WALL: continue

      elif next == EXIT:
        if curr == S: return count
        continue
      
      elif next == BLANK:
        building[nr][nc] = curr, count + 1

      elif curr == S:
        if next == FIRE: continue
        if next == S: continue

      elif curr == FIRE:
        if next == FIRE: continue

      if (nr, nc) in dqset: continue 
      dq.append((nr, nc))
      dqset.add((nr, nc))

  return 'IMPOSSIBLE'

for _ in range(int(input())):
  w, h = map(int, input().split())
  structure = [[*input().strip()] for _ in range(h)]
  print(test(w, h, structure))