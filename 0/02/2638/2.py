from sys import *
input = stdin.readline
setrecursionlimit(10 ** 6)

DIRS = (1, 0), (0, 1), (-1, 0), (0, -1)
EXT, INT, CHZ = '.01'

n, m = map(int, input().split())
paper = [input().split() for _ in range(n)]

def copy(mat): return [row[:] for row in mat]
def out_of_range(r, c): 
  return r not in range(n) or c not in range(m)
def count_value(mat, v): return encode(mat).count(v)
def vis(mat): 
  print()
  for i in mat: print(*i)
  print('#')

def encode(mat): return ';'.join([','.join(p) for p in mat])
def decode(txt): return [t.split(',') for t in txt.split(';')]

def fill_external(paper):
  paper = copy(paper)
  paper = decode(encode(paper).replace(EXT, INT))

  def dfs(r=0, c=0):
    value = paper[r][c]
    if value == INT: paper[r][c] = EXT

    for dr, dc in DIRS:
      nr, nc = r + dr, c + dc
      if out_of_range(nr, nc): continue
      next_value = paper[nr][nc]
      if next_value in [EXT, CHZ]: continue
      dfs(nr, nc)
    
  dfs()
  return paper

def count_contacted(filled, position):
  r, c = position
  count = 0
  for dr, dc in DIRS:
    nr, nc = r + dr, c + dc
    if out_of_range(nr, nc): continue
    if filled[nr][nc] == EXT: count += 1

  return count


def melt_cheeze(paper):
  melted = copy(paper)

  for r in range(n):
    for c in range(m):
      if paper[r][c] != CHZ: continue
      if count_contacted(paper, (r, c)) < 2: continue
      melted[r][c] = EXT
  
  melted = fill_external(melted)
  return melted

count = 0
vis(paper)
melted = fill_external(paper)
vis(melted)

while True:
  count += 1
  melted = melt_cheeze(melted)
  if not count_value(melted, CHZ): break
  print(count)
  vis(melted)

print(count)