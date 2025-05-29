def power(a, b, c):
  if b == 1: return a % c
  div = power(a, b // 2, c)
  sqr = div * div
  if b & 1: sqr *= a
  return sqr % c

print(power(*map(int, input().split())))