from collections import deque
from sys import stdin

input = stdin.readline
offsets = (1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)

def move(n, src, des):
  board = [[-1] * n for _ in range(n)]
  queue = deque([src + (-1,)])

  def out_of_range(r, c):
    return r not in range(n) or c not in range(n)
  
  while queue:
    r, c, count = queue.popleft()
    count += 1
    
    if (r, c) == des: return count
    board[r][c] = count

    for dr, dc in offsets:
      nr, nc = r + dr, c + dc
      if out_of_range(nr, nc): continue
      if board[nr][nc] >= 0: continue

      if (nr, nc, count) in queue: continue
      queue.append((nr, nc, count))

for i in range(int(input())):
  n = int(input())
  src = tuple(map(int, input().split()))
  des = tuple(map(int, input().split()))
  print(move(n, src, des))