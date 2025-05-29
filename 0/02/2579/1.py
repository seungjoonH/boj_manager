from collections import deque
import time


n = int(input())
points = [int(input()) for _ in range(n)]
queue = deque([(0, 0, 0, points[0]), (1, 0, 0, points[1])])
max_point = 0

t = time.time()
c = 0

while queue:
  c += 1
  index, sequence, count, point = queue.popleft()
  max_point = max(point, max_point)
  a, b = index + 1, index + 2

  if a < n and sequence < 1:
    next_element = (a, sequence + 1, count + 1, point + points[a])
    if next_element not in queue: queue.append(next_element)

  if b < n:
    next_element = (b, 0, count + 1, point + points[b])
    if next_element not in queue: queue.append(next_element)

print(max_point)
print(time.time() - t)
print(c)

#15449