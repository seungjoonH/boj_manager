from collections import deque
from sys import stdin
input = stdin.readline

DIRS = (-1, 0), (0, -1), (1, 0), (0, 1)

n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]
maxi = 0

def encode(r, c, trace): return f'{r},{c},{trace}'
def decode(txt): 
  r, c, trace = txt.split(',')
  return (int(r), int(c)), trace
def out_of_range(r, c):
  return r not in range(n) or c not in range(m)

for i in range(n)[::-1]:
  for j in range(m)[::-1]:
    if i + j == 0: maxi = max(maxi, 1); break

    element = encode(i, j, board[i][j])
    queue = deque([element])
    seen = set([element])

    while queue:
      popped = queue.popleft()
      seen.discard(popped)
      (r, c), trace = decode(popped)
      if r + c == 0: maxi = max(maxi, len(trace))

      for dr, dc in DIRS:
        nr, nc = r + dr, c + dc
        if out_of_range(nr, nc): continue
        next_value = board[nr][nc]
        if nr + nc and next_value == board[0][0]: continue
        if next_value in trace: continue
        element = encode(nr, nc, trace + next_value)
        if element in seen: continue
        queue.append(element)
        seen.add(element)

print(maxi)