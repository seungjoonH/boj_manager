from sys import stdin
input = stdin.readline

def minmax(x, y): return max(x, y), min(x, y)

while True:
  a, b, c, d = ipt = list(map(int, input().split()))
  if not sum(ipt): break
  (a, b), (c, d) = map(minmax, (a, c), (b, d))
  a, b = minmax(a, b)
  c, d = minmax(c, d)
  p = int(max(1, min(1, c / a, d / b) * 100))
  print(f'{p}%')