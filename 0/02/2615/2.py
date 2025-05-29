from sys import stdin
input = stdin.readline

N = 19
directions = (0, 1), (1, 0), (1, 1), (-1, 1)
board = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
board = [[0] * (N + 2)] + board + [[0] * (N + 2)]

def has_five(position, color, direction):
  r, c = position
  dr, dc = direction
  nr, nc = r - dr, c - dc

  if board[nr][nc] == color: return False

  for _ in range(5):
    nr += dr; nc += dc
    if board[nr][nc] != color: return False

  nr += dr; nc += dc
  return board[nr][nc] != color

def get_winner():
  for c in range(1, N + 1):
    for r in range(1, N + 1):
      value = board[r][c]
      if not value: continue
      for direction in directions:
        if has_five((r, c), value, direction):
          return f'{value}\n{r} {c}'
  return 0

print(get_winner())