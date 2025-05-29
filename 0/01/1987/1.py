from sys import stdin
input = stdin.readline

DIRS = (-1, 0), (0, -1), (1, 0), (0, 1)

n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]
maxi = 0

def out_of_range(r, c):
  return r not in range(n) or c not in range(m)

for i in range(n)[::-1]:
  for j in range(m)[::-1]:
    queue = {(i, j): board[i][j]}

    while queue:
      next_queue = dict()

      for (r, c), trace in queue.items():
        if r + c == 0: maxi = max(maxi, len(trace))

        for dr, dc in DIRS:
          nr, nc = r + dr, c + dc
          if out_of_range(nr, nc): continue
          next_value = board[nr][nc]
          if nr + nc and next_value == board[0][0]: continue
          if next_value in trace: continue

          next_queue[(nr, nc)] = trace + next_value

      queue = next_queue

print(maxi)