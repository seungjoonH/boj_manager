units = [*map(str, range(10)), *map(chr, range(65, 91))]

n, b = map(int, input().split())
result = ''

while n > 0:
  unit = n % b
  result = units[unit] + result
  n = (n - unit) // b

print(result)