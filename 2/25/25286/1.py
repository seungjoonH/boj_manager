def leap(y): return y % 100 and not y % 4 or not y % 400
def get_date(y, m):
  if m == 1: return y - 1, 12, 31
  elif m == 3: return y, 2, leap(y) and 29 or 28
  return y, m - 1, m in [2, 4, 6, 8, 9, 11] and 31 or 30

for _ in range(int(input())):
  print(*get_date(*map(int, input().split())))