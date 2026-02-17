from heapq import *

n, *a = map(str.split, open(0))
n = int(n[0])
heap = []
problems = sorted(tuple(map(int, t)) for t in a)
mx = 0

for d, v in problems:
  heappush(heap, v)
  if len(heap) > d: heappop(heap)

print(sum(heap))