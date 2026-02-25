from sys import stdin
input = stdin.readline

MAX, MIN = float('inf'), -float('inf')

n = int(input())
se = sorted(tuple(map(int, input().split())) for _ in range(n))
m = 1 + max(e for _, e in se)

calendar = [[0] for _ in range(m)]

def append(s, e):
  r = calendar[s - 1].index(0) if 0 in calendar[s - 1] else -1
  if calendar[s - 1][r]:
    for i in range(m): calendar[i].append(0)
  for i in range(s - 1, e): calendar[i][r] = 1

def get_tb(col):
  if 1 not in col: return MIN, MAX
  return col.index(1), len(col) - col[::-1].index(1) - 1

def get_area(w, b, t):
  if t == MAX or b == MIN: return 0
  return w * (b - t + 1)

for s, e in se: append(s, e)

area = 0
w, t, b = 0, MAX, MIN

for c, col in enumerate(calendar):
  if sum(col):
    w += 1
    ct, cb = get_tb(col)
    t, b = min(ct, t), max(cb, b)

  else:
    area += get_area(w, b, t)
    w, t, b = 0, MAX, MIN

print(area)