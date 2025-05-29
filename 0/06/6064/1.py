def cain(m, n, x, y):
  d = x - y
  while True:
    if x == y: return x
    elif x < y: x += m
    else: y += n
    if d == x - y: return -1

for _ in range(int(input())):
  print(cain(*map(int, input().split())))