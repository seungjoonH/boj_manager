import sys
sys.setrecursionlimit(10 ** 5)

def power(a, x, c):
  if x < 2: return [1, a][x]
  p = power(a, x >> 1, c)
  return (a ** (x % 2) * p * p) % c

a, b, c = map(int, input().split())
print(power(a, b, c))