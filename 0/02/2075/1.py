from heapq import *
from sys import stdin
input = stdin.readline

heap = []
n = int(input())
for _ in range(n):
  for j in map(int, input().split()): 
    heappush(heap, j)
    if len(heap) > n: heappop(heap)

print(heap[0])