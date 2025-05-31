def count(num): return str(num).count('8')

def result(l, r): 
  a, b = l, r
  if len(str(l)) != len(str(r)): return 0

  for i, n in enumerate(str(r)):
    if n != '8': continue
    p = 10 ** (len(str(l)) - i - 1)
    if r - p > l: b -= p

  for i, n in enumerate(str(l)[::-1]):
    if n != '8': continue
    p = 10 ** i
    if l + p < r: a += p
  
  return min(map(count, [a, b]))

print(result(*map(int, input().split())))