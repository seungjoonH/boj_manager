n, *ps = map(int, input().split())
DIRS = { 'E': (0, 1), 'W': (0, -1), 'N': (-1, 0), 'S': (1, 0) }
PROBS = {[*DIRS.keys()][i]: p / 100 for i, p in enumerate(ps[:])}
SIZE = n * 2 + 1

visited = [[0] * SIZE for _ in range(SIZE)]
psum = 0

def dfs(r, c, index, prob):
  global psum
  if index == n: psum += prob; return

  for d, (dr, dc) in DIRS.items():
    if PROBS[d] == .0: continue
    nr, nc = r + dr, c + dc

    if visited[nr][nc]: continue
    visited[nr][nc] = 1
    dfs(nr, nc, index + 1, prob * PROBS[d])
    visited[nr][nc] = 0

visited[n][n] = True
dfs(n, n, 0, 1.0)

print(psum)