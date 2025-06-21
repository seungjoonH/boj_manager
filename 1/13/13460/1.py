from copy import deepcopy
from collections import deque

VOID, WALL, HOLE, RED, BLUE = '.#ORB'
DIRS = R, D, L, U = (0, 1), (1, 0), (0, -1), (-1, 0)

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

red, blue = (0, 0), (0, 0)

def index(l, e): 
  try: return l.index(e)
  except: return -1

for i, row in enumerate(board): 
  r, b = index(row, RED), index(row, BLUE)
  if r > 0: red = (i, r)
  if b > 0: blue = (i, b)

def out_of_range(r, c):
  return r not in range(1, n - 1) or c not in range(1, m - 1)

def move(board, dir, ball):
  (r, c), (dr, dc) = ball, dir
  cr, cc = r, c
  color = board[r][c]
  aim = VOID

  while True:
    nr, nc = cr + dr, cc + dc
    if out_of_range(nr, nc): break
    cur, nxt = board[cr][cc], board[nr][nc]
    aim = nxt

    if nxt not in [VOID, HOLE]: return 0, (cr, cc)
    if cur in [RED, BLUE]:
      board[nr][nc] = board[cr][cc]
      board[cr][cc] = VOID
    cr, cc = nr, nc

    if aim == HOLE: 
      board[cr][cc] = 'O'
      if color == BLUE: return -1, (cr, cc)
      elif color == RED: return 1, (cr, cc)
    
  return 0, (cr, cc)

def tilt(board, dir, red, blue):
  r1, red = move(board, dir, red)
  b, blue = move(board, dir, blue)
  r2, red = move(board, dir, red)
  if -1 in [r1, b, r2]: return -1, red, blue
  elif 1 in [r1, b, r2]: return 1, red, blue
  return 0, red, blue

def escape():
  queue = deque()
  queue.append((deepcopy(board), R, red, blue, 0))
  queue.append((deepcopy(board), D, red, blue, 0))
  queue.append((deepcopy(board), L, red, blue, 0))
  queue.append((deepcopy(board), U, red, blue, 0))

  mn = float('inf')

  while queue:
    cboard, d, r, b, c = queue.popleft()
    res, nr, nb = tilt(cboard, d, r, b)
    if res < 0: continue
    elif res > 0: return c + 1
    if c > 9: return -1

    if d in [L, R]:
      queue.append((deepcopy(cboard), U, nr, nb, c + 1))
      queue.append((deepcopy(cboard), D, nr, nb, c + 1))
    elif d in [U, D]: 
      queue.append((deepcopy(cboard), L, nr, nb, c + 1))
      queue.append((deepcopy(cboard), R, nr, nb, c + 1))

  return mn

print(escape())