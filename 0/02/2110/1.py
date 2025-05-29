from sys import stdin

input = stdin.readline
n, c = map(int, input().split())
houses = sorted([
  int(input().replace('\n', '')) 
  for _ in range(n)
])

first, last = houses[0], houses[-1]
routers = [first, last]

def set_router(start, end):
  left, right = start, end
  if left >= right: return
  if len(routers) == c: return

  mid = (start + end) // 2

  for dif in range(mid):
    if (mid - dif) in houses:
      if mid - dif not in routers:
        routers.append(mid - dif)
        left = mid - dif
        break
    elif (mid + dif) in houses:
      if mid + dif not in routers:
        routers.append(mid + dif)
        right =  mid + dif
        break

  return set_router(left, right)

set_router(first, last)

res = last - first
for i in range(len(routers) - 1):
  res = min(abs(routers[i + 1] - routers[i]), res)

print(res)