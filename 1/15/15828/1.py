from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
queue = deque()

while True:
  i = int(input())
  if i < 0: break

  if i and len(queue) < n: queue.append(i)
  if not i and queue: queue.popleft()

if queue: print(*queue)
else: print('empty')