import math

a, b = map(int, input().split())
cache = {1: 1, 2: 2, 3: 4}

def count_1(n):
  if n < 1: return 0
  if n in cache: return cache[n]

  lgn = int(math.log2(n))
  p = 1 << lgn

  cache[n] = lgn * (p >> 1) + n - p + 1 + count_1(n - p)
  return cache[n]

print(count_1(b) - count_1(a - 1))