from heapq import *
from sys import stdin
input = stdin.readline

heap = []

for _ in range(int(input())):
  x = int(input())
  if x: heappush(heap, (abs(x), x)); continue
  a, x = heappop(heap) if heap else (0, 0)
  print(x)