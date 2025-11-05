n = int(input())
for i in range(2 * n - 1):
  s = min(i + 1, 2 * n - i - 1)
  b = 2 * (n - s)
  print('*' * s + ' ' * b + '*' * s)