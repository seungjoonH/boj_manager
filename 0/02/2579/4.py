from sys import stdin
input = stdin.readline
import time

n = int(input())
points = [int(input()) for _ in range(n)]
memory = set([(0, 0, 0, points[0]), (1, 0, 0, points[1])])
max_point = 0

def append(element):
  if element in memory: return
  memory.add(element)


t = time.time()
c = 0

while memory:
  c += 1
  index, sequence, count, point = memory.pop()
  max_point = max(point, max_point)
  a, b = index + 1, index + 2

  if a < n and sequence < 1:
    append((a, sequence + 1, count + 1, point + points[a]))

  if b < n:
    append((b, 0, count + 1, point + points[b]))

print(max_point)
print(time.time() - t)
print(c)

# 15449