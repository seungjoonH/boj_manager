from sys import stdin

input = stdin.readline
n, c = map(int, input().split())
houses = sorted(int(input()) for _ in range(n))

first, last = houses[0], houses[-1]
routers = [first, last]

def set_router(start, end):
  left, right = houses.index(start), houses.index(end)

  if start >= end: return
  if len(routers) == c: return

  mid = (start + end) // 2
  dif = (end - start) // 2
  near = -1

  for i in range(left + 1, right):
    h = houses[i]

    if abs(h - mid) <= dif:
      near = h
      dif = abs(h - mid)

  if near < 0: return

  if near - start > end - near: end = near
  else: start = near

  routers.append(near)

  return set_router(start, end)

set_router(first, last)

routers.sort()
res = last - first
for i in range(len(routers) - 1):
  res = min(abs(routers[i + 1] - routers[i]), res)

print(res)