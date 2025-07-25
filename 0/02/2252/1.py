from collections import deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
graph = dict()

def get(key): return graph[key] if key in graph else []
def add(a, b):
  if a in graph: graph[a].append(b)
  else: graph[a] = [b]

for _ in range(1, m + 1): add(*map(int, input().split()))

result = []
in_degrees = [0] * n
queue = deque([])

def degree(node): return in_degrees[node - 1]
def increase(node): in_degrees[node - 1] += 1
def decrease(node): in_degrees[node - 1] -= 1

for i in range(1, n + 1):
  for node in get(i): increase(node)

for i in range(1, n + 1):
  if not degree(i): queue.append(i)

while queue:
  node = queue.popleft()
  result.append(node)

  for adj in get(node): 
    decrease(adj)
    if degree(adj): continue
    queue.append(adj)

print(*result)