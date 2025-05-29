prime_cache = set([2, 3, 5, 7, 11, 13])

def is_prime(num):
  if num == 1: return 0
  if num in prime_cache: return 1
  
  for i in range(2, int(num ** .5) + 1):
    if not (num % i): return 0

  prime_cache.add(num)
  return 1

def count_factors(num):
  if is_prime(num): return 1
  
  factor = 1
  for i in range(int(num ** .5), 1, -1):
    if not (num % i): factor = i; break
  
  x_factor = count_factors(factor)
  if factor ** 2 == num: return 2 * x_factor
  return x_factor + count_factors(num // factor)

def under_prime(num):
  if is_prime(num): return 0
  return is_prime(count_factors(num))

a, b = map(int, input().split())
print(sum(map(under_prime, range(a, b + 1))))