def f(n, c = 0):
  if n < 10: return c
  return f(eval('*'.join(str(n))), c + 1)
print(f(int(input())))