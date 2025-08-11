from sys import stdin
input = stdin.readline

def is_disjoint(a, b):
  return a[2] < b[0] or b[2] < a[0] or a[3] < b[1] or b[3] < a[1]

Lx, Ly, n = map(int, input().split())

rects = [(0, 0, 0, Ly - 1, Lx - 1)]
ans = 0

for _ in range(n):
  lx, ly, lz, px, py = map(int, input().split())
  y0, y1 = py, py + ly - 1
  x0, x1 = px, px + lx - 1

  base = 0
  for rz, ry0, rx0, ry1, rx1 in rects:
    if is_disjoint((ry0, rx0, ry1, rx1), (y0, x0, y1, x1)): continue
    if rz > base: base = rz

  z = base + lz
  if z > ans: ans = z
  rects.append((z, y0, x0, y1, x1))

print(ans)