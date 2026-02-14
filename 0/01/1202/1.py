from sys import stdin
from heapq import *

input = stdin.readline

n, k = map(int, input().split())
jewels = sorted(tuple(map(int, input().split())) for _ in range(n))
bags = sorted(int(input()) for _ in range(k))

heap = []
i = value = 0

for bag in bags:
  while i < n: 
    m, v = jewels[i]
    if m > bag: break
    i += 1
    heappush(heap, (-v, m))

  if heap: value -= heappop(heap)[0]

print(value)