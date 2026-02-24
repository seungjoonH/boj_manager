MINE, BLANK, OPEN = '*.x'
DIRS = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

n = int(input())
board = [input() for _ in range(n)]
opened = [input() for _ in range(n)]
result = [[BLANK] * n for _ in range(n)]

over = False

def gameover(open, mine):
  global over
  if not over and open and mine: over = True

def is_mine(r, c):
  if r not in range(n) or c not in range(n): return 0
  mine = board[r][c] == MINE
  print(r, c)
  gameover(opened[r][c] == OPEN, mine)
  return mine

def count(r, c):
  return sum(is_mine(r + dr, c + dc) for dr, dc in DIRS)

for r in range(n):
  for c in range(n):
    if over and board[r][c] == MINE: result[r][c] = MINE
    elif opened[r][c] == OPEN: result[r][c] = count(r, c)
    
for row in result: print(*row, sep='')