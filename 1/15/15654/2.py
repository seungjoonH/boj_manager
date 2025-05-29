from collections import deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
numbers = sorted(map(int, input().split()))

def permutations(numbers, r):
  result = []
  queue = deque([([], [False] * n)])

  while queue:
    path, used = queue.popleft()
    print(path, [int(i) for i in used])
    if len(path) == r: result.append(path[:]); continue
    for i in range(n):
      if used[i]: continue
      used[i] = True
      queue.append((path + [numbers[i]], used[:]))
      used[i] = False

  return result

for t in permutations(numbers, m): print(*t)