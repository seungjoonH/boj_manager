import math

def get_factors(num):
  factors = {1: 1}
  n, d = num, 0
  while d * d <= num:
    c = 0; d += 2 - (d == 2)
    while not n % d: n //= d; c += 1
    if c: factors[d] = c

  if n > 1: factors[n] = factors.get(n, 0) + 1
  return factors

def totient(factor):
  base, exp = factor
  if base == 1: return 1
  if exp == 1: return base - 1
  return int(base ** exp * (1 - 1 / base))

print(math.prod(list(map(totient, get_factors(int(input())).items()))))