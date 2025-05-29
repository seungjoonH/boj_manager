r1, c1, r2, c2 = map(int, input().split())
rows = r2 - r1 + 1
cols = c2 - c1 + 1

def get_number(r, c):
  sr, sc = map(lambda x: 2 * (x >= 0) - 1, [r, c])
  if abs(r) >= abs(c): return 1 + 2 * r * (2 * r + 1) + (r + c) * sr
  return 2 * c * (2 * c - 1) + 2 - 2 * c * sc + (c - r) * sc - 1

numlen = len(str(max(
  get_number(r1, c1), get_number(r1, c2),
  get_number(r2, c1), get_number(r2, c2),
)))

fmt = '{:' + str(numlen) + 'd}'

for i in range(rows):
  for j in range(cols):
    if j: print(end=' ')
    number = get_number(i + r1, j + c1)
    print(fmt.format(number), end='')
  print()