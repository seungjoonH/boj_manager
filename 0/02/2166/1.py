from sys import stdin
input = stdin.readline

def area(a, b, c):
  ax, ay = a
  bx, by = b
  cx, cy = c
  return .5 * ((ax * by + bx * cy + cx * ay) - (ay * bx + by * cx + cy * ax))

n = int(input())

x1 = y1 = x2 = y2 = x3 = y3 = 0

for _ in range(n):
  x, y = map(int, input().split())
