MINE, BLANK, OPEN = '*.x'
DIRS = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

n = int(input())
board = [input() for _ in range(n)]
opened = [input() for _ in range(n)]
result = [[BLANK] * n for _ in range(n)]

over = False

def is_mine(r, c):
  if r not in range(n) or c not in range(n): return 0
  return board[r][c] == MINE

def count(r, c):
  return sum(is_mine(r + dr, c + dc) for dr, dc in DIRS)

for r in range(n):
  if over: break
  for c in range(n):
    if opened[r][c] == OPEN and is_mine(r, c): 
      over = True; break

for r in range(n):
  for c in range(n):
    if over and is_mine(r, c): result[r][c] = MINE
    elif opened[r][c] == OPEN: result[r][c] = count(r, c)
    
for row in result: print(*row, sep='')