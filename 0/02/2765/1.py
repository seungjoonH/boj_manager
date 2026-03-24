from sys import stdin
input = stdin.readline

PI = 3.1415927
i = 0

while True:
  d, r, s = map(float, input().split())
  if not r: break

  i += 1
  dist = d / 63360 * PI * r
  mph = dist / s * 3600
  print(f'Trip #{i}: {dist:.2f} {mph:.2f}')
