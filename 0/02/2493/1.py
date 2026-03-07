from collections import deque
from sys import stdin
input = stdin.readline

n = int(input())
towers = [*map(int, input().split())]
stack = deque()
res = dict()

for i in range(1, len(towers)):
  curr, next = towers[-i], towers[~i]
  stack.append((n - i, curr))
  if stack[-1][1] > next: continue
  
  while stack and stack[-1][1] < next:
    pi, p = stack.pop()
    res[pi] = n - i

print(*[res[i] if i in res else 0 for i in range(n)])