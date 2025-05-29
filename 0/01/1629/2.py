import sys
sys.setrecursionlimit(10 ** 5)

def power(a, x, c):
  if x < 2: return [1, a % c][x]
  p = power(a, x >> 1, c)
  p = (p * p) % c
  if x % 2: p = (p * a) % c
  return p

print(power(*map(int, input().split())))
