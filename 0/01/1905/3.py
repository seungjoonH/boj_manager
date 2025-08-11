from itertools import islice
from sys import stdin
input = stdin.readline

Lx, Ly, n = map(int, input().split())
warehouse = [[0] * Lx for _ in range(Ly)]

def place(c, lx, ly, lz, px, py):
  z = lz + max(max(islice(row, px, px + lx)) for row in islice(warehouse, py, py + ly))
  if c == n - 1: return z
  
  fill = [z] * lx
  for i in range(py, py + ly): warehouse[i][px:px + lx] = fill
  return z

print(max(place(i, *map(int, input().split())) for i in range(n)))