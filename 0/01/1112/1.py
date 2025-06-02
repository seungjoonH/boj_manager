def convert(num, notation):
  if not num: return 0
  n, result = num, ''
  negative = n < 0 and notation > 0
  if negative: n = abs(n)
  while abs(n) > 0:
    n, r = divmod(n, notation)
    if r < 0: r -= notation; n += 1
    result = str(r) + result
  return '-' * negative + result

print(convert(*map(int, input().split())))