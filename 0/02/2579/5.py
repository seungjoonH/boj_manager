from sys import stdin
from collections import deque
import time

input = stdin.readline

n = int(input())
points = [int(input()) for _ in range(n)]
queue = deque([(0, 0, points[0]), (1, 0, points[1])])
seen = set()
max_point = 0

def append(element):
  if element in seen: return
  queue.append(element)
  seen.add(element)

t = time.time()
c = 0

while queue:
  c += 1
  index, sequence, point = queue.popleft()
  max_point = max(point, max_point)
  a, b = index + 1, index + 2

  if a < n and sequence < 1:
    append((a, sequence + 1, point + points[a]))

  if b < n:
    append((b, 0, point + points[b]))

print(max_point)
print(time.time() - t)
print(c)

# 15449