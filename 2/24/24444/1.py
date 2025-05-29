from collections import deque
from sys import stdin
input = stdin.readline

n, m, r = map(int, input().split())
dq = deque([r])

graph = {}
for _ in range(m):
  u, v = map(int, input().split())
  if u not in graph: graph[u] = []
  if v not in graph: graph[v] = []
  
  graph[u].append(v)
  graph[v].append(u)

for k in graph: graph[k].sort()

count, visited = 0, [0] * n

while dq:
  node = dq.popleft()
  if visited[node - 1]: continue

  count += 1
  visited[node - 1] = count

  for child in graph[node]: dq.append(child)

print(*visited, sep='\n')