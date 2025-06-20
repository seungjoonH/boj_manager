from sys import stdin
input = stdin.readline

def area(a, b, c):
  (ax, ay), (bx, by), (cx, cy) = a, b, c
  return ((ax * by + bx * cy + cx * ay) - (ay * bx + by * cx + cy * ax)) / 2

n = int(input())
coords = [tuple(map(int, input().split())) for _ in range(n)]

s = sum(area(coords[0], coords[i], coords[i + 1]) for i in range(1, n - 1))
print(round(abs(s), 1))