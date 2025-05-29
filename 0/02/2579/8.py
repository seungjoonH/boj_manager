from sys import stdin
input = stdin.readline

n = int(input())
points = [int(input()) for _ in range(n)]

memory = {(0, 0): points[0]}
if n > 1: memory[(1, 0)] = points[1]
max_point = 0

while memory:
  next_memory = dict()

  for (index, sequence), point in memory.items():
    
    if index == n - 1: max_point = max(point, max_point)
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