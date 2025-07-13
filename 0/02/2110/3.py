from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10 ** 6)

n, c = map(int, input().split())
houses = sorted([int(input()) for _ in range(n)])

def installable(distance):
  count, last = 1, houses[0]
  for i in range(1, len(houses)):
    if houses[i] - last < distance: continue
    last = houses[i]
    count += 1
  return count >= c

def search(low=1, high=houses[-1] - houses[0]):
  if low > high: return high
  mid = (low + high) // 2

  if installable(mid): return search(mid + 1, high)
  return search(low, mid - 1)

print(search())