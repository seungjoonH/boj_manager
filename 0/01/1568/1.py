def f(x):
  if x < 3: return x
  n = int(((8 * x + 1) ** .5 - 1) / 2)
  s = n * -~n // 2
  return n + f(x - s)

print(f(int(input())))