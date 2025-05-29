from sys import stdin
input = stdin.readline

N = 19
directions = (0, 1), (1, 0), (1, 1), (-1, 1)
board = [list(map(int, input().split())) for _ in range(N)]

def out_of_range(r, c):
  return r not in range(N) or c not in range(N)

def has_five(position, color, direction):
  r, c = position
  dr, dc = direction
  nr, nc = r - dr, c - dc

  if not out_of_range(nr, nc) and board[nr][nc] == color:
    return False

  for _ in range(5):
    nr += dr; nc += dc
    if out_of_range(nr, nc): return False
    if board[nr][nc] != color: return False

  nr += dr; nc += dc
  return out_of_range(nr, nc) or board[nr][nc] != color

def get_winner():
  for c in range(N):
    for r in range(N):
      value = board[r][c]
      if not value: continue
      for direction in directions:
        if has_five((r, c), value, direction):
          return f'{value}\n{r + 1} {c + 1}'
  return 0

print(get_winner())