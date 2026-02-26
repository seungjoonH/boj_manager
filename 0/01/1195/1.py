MAX = float('inf')

a, b = map(str.strip, open(0))
a = [*map(int, a)]
b = [*map(int, b)]
la, lb = len(a), len(b)

def merge(a, b):
  m = max(len(a), len(b))
  ai, bi = [0] * m, [0] * m
  ai[0:len(a) - 1] = a[:]
  bi[0:len(b) - 1] = b[:]
  return [*map(sum, zip(ai, bi))]

def isfit(c): return all(map(lambda x: x <= 3, c))
def trim(c): return [*filter(bool, c)]

width = MAX

for i in range(1 - la, lb):
  ai, bi = a[:], b[:]
  if i <= 0: bi = [0] * -i + b[:]
  if i > 0: ai = [0] * i + a[:]

  ci = merge(ai, bi)
  if isfit(ci): width = min(width, len(trim(ci)))

if width == MAX: width = la + lb

print(width)