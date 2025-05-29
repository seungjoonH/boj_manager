from sys import stdin
import time

input = stdin.readline

n = int(input())
points = [int(input()) for _ in range(n)]
memory = {(0, 0): points[0], (1, 0): points[1]}
max_point = 0

t = time.time()
c = 0

while memory:
  next_memory = dict()

  for (index, sequence), point in memory.items():
    c += 1
    
    max_point = max(point, max_point)
    a, b = index + 1, index + 2

    if a < n and sequence < 1:
      e = (a, sequence + 1)
      p = next_memory[e] if e in next_memory else 0
      next_memory[e] = max(p, point + points[a])

    if b < n:
      e = (b, 0)
      p = next_memory[e] if e in next_memory else 0
      next_memory[e] = max(p, point + points[b])

  memory = next_memory

print(max_point)
print(time.time() - t)
print(c)

# 15449