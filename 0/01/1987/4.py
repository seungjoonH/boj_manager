from collections import deque
from sys import stdin
input = stdin.readline

DIRS = (-1, 0), (0, -1), (1, 0), (0, 1)

n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]
maxi = 0

def encode(r, c, trace): return f'{r},{c},{trace}'
def decode(txt): return list(map(int, txt.split(',')))
def out_of_range(r, c): return r not in range(n) or c not in range(m)
def to_bit(c): return 1 << (ord(c) - ord('A'))

def bfs(i, j):
  global maxi

  value = board[i][j]
  if value == board[0][0]: return

  element = encode(i, j, to_bit(board[i][j]))
  queue = deque([element])
  seen = set([element])

  while queue:
    popped = queue.popleft()
    seen.discard(popped)
    r, c, trace = decode(popped)
    if r + c == 0: 
      maxi = max(maxi, bin(trace).count('1'))
      if maxi == 26: return

    for dr, dc in DIRS:
      nr, nc = r + dr, c + dc
      if out_of_range(nr, nc): continue
      next_value = board[nr][nc]
      next_bit = to_bit(next_value)

      if nr + nc and next_value == board[0][0]: continue
      if next_bit & trace: continue
      element = encode(nr, nc, next_bit | trace)

      if element in seen: continue
      queue.append(element)
      seen.add(element)

for i in range(n)[::-1]:
  for j in range(m)[::-1]:
    if maxi == 26: break
    if i + j == 0: maxi = max(maxi, 1); break
    bfs(i, j)

print(maxi)