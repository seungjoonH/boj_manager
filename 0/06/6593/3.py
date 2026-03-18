from collections import deque
from sys import stdin
input = stdin.readline

START, END, WALL, BLANK = 'SE#.'
DIRS = (0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)

def test(t, building, coords):
  l, r, c = t
  sl, sr, sc = coords[START]

  dq = deque([(sl, sr, sc, 0)])
  building[sl][sr][sc] = 0

  while dq:
    cl, cr, cc, count = dq.popleft()
    building[cl][cr][cc] = count

    for dh, dr, dc in DIRS:
      nl, nr, nc = cl + dh, cr + dr, cc + dc
      if not (0 <= nl < l): continue
      if not (0 <= nr < r): continue
      if not (0 <= nc < c): continue
      next = building[nl][nr][nc]
      if next == END: return count + 1
      if next != BLANK: continue
      
      building[nl][nr][nc] = count + 1
      dq.append((nl, nr, nc, count + 1))

while True:
  row = input().strip()
  if row == '0 0 0': break

  l, r, c = map(int, row.split())
  building = []
  coords = dict()

  for i in range(l):
    floor = []
    for j in range(r):
      row = []
      for k, cell in enumerate(input().strip()):
        row.append(cell)
        if cell in START + END: coords[cell] = (i, j, k)
      floor.append(row)
    
    input()
    building.append(floor)

  res = test((l, r, c), building, coords)
  print([f'Escaped in {res} minute(s).', 'Trapped!'][res is None])