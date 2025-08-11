from sys import stdin
input = stdin.readline

Lx, Ly, n = map(int, input().split())
warehouse = [[0] * Lx for _ in range(Ly)]

def place(lx, ly, lz, px, py):
  z = lz + max([max(row[px:px + lx]) for row in warehouse[py:py + ly]])
  for i in range(py, py + ly): warehouse[i][px:px + lx] = [z] * lx
  return z

print(max(place(*map(int, input().split())) for _ in range(n)))