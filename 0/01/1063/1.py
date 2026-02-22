k, r, n = input().split()
n = int(n)

MAX_SIZE = 8
DIRS = {
   'R': ( 0, 1),  'L': ( 0, -1),
   'B': (-1, 0),  'T': ( 1,  0),
  'RT': ( 1, 1), 'LT': ( 1, -1),
  'RB': (-1, 1), 'LB': (-1, -1),
}

def to_coords(pos):
  c, r = pos
  return int(r) - 1, ord(c) - 65

def to_pos(r, c):
  return chr(c + 65) + str(r + 1)

board = [[0] * MAX_SIZE for _ in range(MAX_SIZE)]
(kr, kc), (rr, rc) = map(to_coords, (k, r))

def move(d):
  global kr, kc, rr, rc
  cr, cc = kr, kc

  dr, dc = DIRS[d]
  if not (0 <= cr + dr < MAX_SIZE): return
  if not (0 <= cc + dc < MAX_SIZE): return

  nr, nc = cr + dr, cc + dc
  
  if board[nr][nc] == 'R':
    if not (0 <= nr + dr < MAX_SIZE): return
    if not (0 <= nc + dc < MAX_SIZE): return
    rr, rc = nr + dr, nc + dc
    board[rr][rc] = 'R'
  
  kr, kc = nr, nc
  board[kr][kc] = 'K'
  board[cr][cc] = 0

board[kr][kc] = 'K'
board[rr][rc] = 'R'

for _ in range(n): move(input())

print(to_pos(kr, kc))
print(to_pos(rr, rc))