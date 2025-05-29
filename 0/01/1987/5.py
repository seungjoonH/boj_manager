from sys import *
input = stdin.readline
setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def out_of_range(r, c): return r not in range(n) or c not in range(m)
def to_bit(c): return 1 << (ord(c) - ord('A'))

memory = dict()

def dfs(r, c, trace):
  key = f'{r},{c},{trace}'
  if key in memory: return memory[key]

  maxi = 0
  for dr, dc in DIRS:
    nr, nc = r + dr, c + dc
    if out_of_range(nr, nc): continue
    value = to_bit(board[nr][nc])
    if trace & value: continue
    maxi = max(maxi, dfs(nr, nc, trace | value))

  memory[key] = maxi + 1
  return maxi + 1

result = dfs(0, 0, to_bit(board[0][0]))
print(result)
