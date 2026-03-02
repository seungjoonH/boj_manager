from sys import stdin
input = stdin.readline

DAYS = 365

n = int(input())
se = sorted(tuple(map(int, input().split())) for _ in range(n))
calendar = [0] * (DAYS + 1)

for s, e in se: 
  for i in range(s, e + 1): calendar[i] += 1

width = height = area = 0

for i in range(DAYS):
  count = calendar[i]

  if count:
    width += 1
    height = max(height, count)

  else:
    area += width * height
    width = height = 0

print(area)