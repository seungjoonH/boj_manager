from collections import deque

n = int(input())
words = deque(sorted([input() for _ in range(n)]))
subset = [words.pop()]

while words:
  prefix = subset[-1]
  current = words.pop()
  if current == prefix[:len(current)]: continue
  subset.append(current)
  prefix = current

print(len(subset))